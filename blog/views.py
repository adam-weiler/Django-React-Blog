from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from blog.models import * #Importing the classes from models.py file.


def root(request): # Redirects to http://localhost:8000/home/
    return HttpResponseRedirect('/home')

# # def home_page(request): # http://localhost:8000/home/
# #     context = { 'blog_articles': Article.objects.all().order_by('-published_date'), 'blog_topics': Topic.objects.all() } #The - in published_date means order from newest to oldest.

# #     response = render(request, 'index.html', context)
# #     return HttpResponse(response)

# def show_all(request):
#     context = { 'blog_articles': Article.objects.all().order_by('-published_date'), 'blog_topics': Topic.objects.all() } #The - in published_date means order from newest to oldest.

#     response = render(request, 'articles.html', context)
#     return HttpResponse(response)

# def show_article(request, id): #Load a single article page based on id.
#     article = Article.objects.get(pk=id)
#     form = CommentForm()
#     # form.article = article # assoicate the comment to the article somehow
#     return render(request, 'article.html', {
#         'article': article, 
#         'form': form
#     })



# def new_article(request):
#     form = ArticleForm()
#     context = {"form": form}
#     return render(request, "article_form.html", context)


# def create_article(request):
#     form = ArticleForm(request.POST)

#     if form.is_valid():
#         form.save()
#         return redirect(reverse("show_all"))
#     else:
#         context = {"form": form}
#         return render(request, "article_form.html", context)



# def create_comment(request, article_id):
#     article = Article.objects.get(pk=article_id)
#     form = CommentForm(request.POST)

#     comment = form.save(commit=False)
#     comment.article = article
#     comment.save()
#     return redirect(reverse("show_article", args=[article_id]))

#     # # pass
#     # article_id = request.POST['article']
#     # article = Article.objects.get(pk=article_id)

#     # form = CommentForm(request.POST)
#     # context = {'article': article, 'form':form}

#     # if form.is_valid():
#     #     new_comment = form.save(commit=False)
#     #     # new_comment.article = 


#     # article_id = request.POST['article']
#     # # 
#     # article = Article.objects.get(pk=article_id)
#     # # breakpoint()
#     # # form.fields.append({'article_id':'article'}) #Sets the foreign key as the article object.

#     # # if form.is_valid():
#     #     # comment = form.save(commit=False)
#     #     # comment.message = message
    
#     # # form.article = article_id
#     # form.save()

#     # response = render(request, 'article.html', context)
#     # return HttpResponse(response)

#     # # form = CommentForm(request.POST)
#     # # form.save()

#     # # context = {'article': article}
#     # # response = render(request, 'article.html', context)
#     # # return HttpResponse(response)


import logging
import os

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )