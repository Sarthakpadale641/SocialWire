from django.shortcuts import redirect, render, get_object_or_404
from .models import Tweet, SavedTweet, ViewHistory
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

# Helper to get context with saved IDs
def get_common_context(request, tweets):
    context = {'tweets': tweets}
    if request.user.is_authenticated:
        saved_ids = SavedTweet.objects.filter(user=request.user).values_list('tweet_id', flat=True)
        context['saved_tweet_ids'] = set(saved_ids)
    return context

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', get_common_context(request, tweets))

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.user.is_authenticated:
        # Record history
        ViewHistory.objects.update_or_create(user=request.user, tweet=tweet)
    
    # Check if saved
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedTweet.objects.filter(user=request.user, tweet=tweet).exists()
        
    return render(request, 'tweet_detail.html', {'tweet': tweet, 'is_saved': is_saved})

@login_required
def tweet_save(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    saved_tweet, created = SavedTweet.objects.get_or_create(user=request.user, tweet=tweet)
    
    if not created:
        # If already exists, toggle (delete)
        saved_tweet.delete()
        
    # Redirect back to where the user came from
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def saved_list(request):
    saved_tweets = SavedTweet.objects.filter(user=request.user).select_related('tweet').order_by('-created_at')
    tweets = [s.tweet for s in saved_tweets]
    return render(request, 'tweet_list.html', get_common_context(request, tweets))

@login_required
def history_list(request):
    # Get recent unique history
    history = ViewHistory.objects.filter(user=request.user).select_related('tweet').order_by('-viewed_at')
    # Deduplicate in python to preserve order if needed, but select_related is efficient. 
    # Since ViewHistory updates 'viewed_at' on revisit (update_or_create), duplicates shouldn't be a major issue if logic holds.
    tweets = [h.tweet for h in history]
    return render(request, 'tweet_list.html', get_common_context(request, tweets))

def discover_list(request):
    query = request.GET.get('q')
    if query:
        tweets = Tweet.objects.filter(
            Q(text__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        # Random sample
        tweets = Tweet.objects.all().order_by('?')[:20]
        
    return render(request, 'tweet_list.html', get_common_context(request, tweets))