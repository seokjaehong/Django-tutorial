from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request) :
    #가장 최근 발행된 최대 4개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context= {
        'latest_question_list' : latest_question_list,
    }
    #render를 쓰는방식
    return render(request,'polls/index.html',context)

    # #template을 명시적으로 불러와 rendering
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context,request))

    ##쉼표 단위로 구분된 QUESTION목록에 대한 각 항목의 question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in latest_question_list])
    #



def detail(request, question_id):
    '''
    question_id에 해당하는 question객체를 템플릿에 전달
    key : "question"
    1.템플릿에서는 전달받은 question의 question_text를 출력
    2.question이 가진 모든 choice들을 ul>li로 출력
    :param request:
    :param question_id:
    :return:
    '''
    question = Question.objects.get(pk=question_id)
    context = {
        'question' : question
    }
    return render(request,'polls/detail.html', context)

    # return HttpResponse("You're looking at question %s. " % question_id)

def results(request, question_id):
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)



