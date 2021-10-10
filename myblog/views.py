from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from .models import Post, Category, Comment
from .forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# def home(request):
#     return render(request, 'myblog/home.html', {})
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:

        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'myblog/category.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


def CategoryListView(request):
    cat_list = Category.objects.all()
    return render(request, 'myblog/category_list.html', {'cat_list': cat_list})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'myblog/detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        like_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_post.total_likes()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        liked = False
        if like_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myblog/add_post.html'

    # fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'myblog/add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'myblog/post_update.html'
    # fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'myblog/delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    template_name = 'myblog/add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)