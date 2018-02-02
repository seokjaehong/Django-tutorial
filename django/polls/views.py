from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Choice


def index(request):
    # 가장 최근에 발행된 최대 5개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # render를 사용
    return render(request, 'polls/index.html', context)

    # template을 명시적으로 불러와 rendering
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))

    # 쉼표단위로 구분된 Question목록의
    #   각 항목의 question_text로 만들어진 문자열을 리턴
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)


def detail(request, question_id):
    """
    question_id에 해당하는 Question객체를 템플릿에 전달
        key: "question"
        template: polls/templates/polls/detail.html
    템플릿에서는
    1. 전달받은 question의 question_text를 출력
        {{ question.question_text }}
    2. question이 가진 모든 Choice들을 ul > li로 출력
        {% for choice in question.choice_set.all %}
    :param request:
    :param question_id:
    :return:
    """
    # try:
    #     # question을 get()시도
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     # DoesNotExist예외가 발생 시
    #     # Http404에러를 발생시키면서 메시지를 전달
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):

    '''
    question id에 해당하는 question 객체 한개를 넘겨서
    polls/result.html에서
    question에 속한 choice들의 목록을 보여주면서 각 항목의 votes값을 출력

    :param request:
    :param question_id:
    :return:
    '''
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    """
    1.request.POST의 choice 키에 온 value를
    httpresponse로 출력
    2. choice객체의 votes값을 1 증가 시키고 db에 저장
    3. 이후 question_id 에 해당하는 result뷰로 redirect
    :param request:
    :param question_id:
    :return:
    """
    # choice = request.POST['choice']
    # choice = request.POST()


    #request.POST의 name(choice)에 온 value를
    choice_pk = request.POST['choice']
    #pk로 가지는 Choice객체 choice
    choice = Choice.objects.get(pk=choice_pk)
    #vote값 1증가
    choice.votes+=1
    choice.save()

    return redirect(
        'polls:results',
        question_id=question_id
    )

    # return HttpResponse(choice)

    # return HttpResponse("You're voting on question %s." % question_id)