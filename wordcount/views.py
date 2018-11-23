from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse("<h1>This is Home Page</h1>")
    # return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Hi User'})


def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    # print(word_list)
    word_length=(len(word_list))

    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] =1

    sorted_list= sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return  render(request, 'count.html', {'fulltext':data, 'Totalword':word_length, 'worddictionary': sorted_list})


def about(request):
    return render(request, 'about.html')
