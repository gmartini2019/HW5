import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.

    '''
    ASK KUNAL ABOUT THE APPROXIMATION
    '''

    '''CHECK THE CALCULATION - 1 decimal by factor of 10 OR COULD BE CORRECT'''
    answers['(c)'] = 0.1
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5 * math.log((1 - p) / p)"

    # type: float
    # the answer should be correct to 3 significant digits
    '''ADD ENTIRE NUMBER'''
    answers['(d) Weight influence'] = 1.5275252316519468
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    '''ASK KUNAL IF THIS IS A GOOD ANSWER'''

    # type: explain_string
    answers['Explain'] = '''This INTUITIVELY sounds like what a machine learning ensemble method would do. But it isn't. Each classifier, big or small, must have the ability to learn from the mistakes it makes. The coin flip learns absolutely nothing.
    In addition, coin flipping produces a PURELY random value with no correlation to the stock market outcomes'''
    
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    '''ASK KUNAL ABOUT THIS'''
    # type: eval_float

  

    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = 'For both of them, TPR=FPR, so they are both placed on the ROC"s random guess line. Therefore, there is no indication that C2 is better than C1. It might have douple the TPR, but it also has double the FPR.'

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = '''Precision and recall (especially precision) can provide more insights into the effectiveness of a classifier in such situations where one class is significantly underrepresented.'''
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = '''Although C2 has a higher FPR, it also has a higher Recall/TPR and F1 measure, showing that it is more capable of classifying positive cases.
    Even though they have the same precision, C2 is better at identifying positive cases overall.'''

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = '''This option is much more comprehensive than the other:
    Precision accounts for the accuracy of positive predictions.
    Recall measures the correctness of positive identification
    F1 measure's balance of precision and recall.
    It's a better all around method.'''

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C2"


    '''It needs to be coherent with question 2'''

    # type: explain_string
    answers['(iii) best classifier, explain'] = '''C2 has the highest F1 measure, which we have established is the most important metric. However, if the goal is to maintain
    a healthy balance between the rates of true and false positives, then TPR and FPR might be a better choice.'''
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}
    # type: eval_float
    answers['(a) precision for C0'] = "(100 * p) / (1000 * p)"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "2 * ((0.1 * p) / (0.1 + p))"

    '''ASK KUNAL ABOUT p'''

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'unknown'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']

    '''ASK KUNAL IF THESE VALUES LOOK RIGHT'''

    metrics = {
        "recall" : 0.5333,
        "precision" : 0.6154,
        "F-measure": 0.5714,
        "accuracy": 0.88,
    }

    answers['(i) metrics'] = metrics

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'precision'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = '''
    Precision is the worst because it focuses only on predicting sunny days, without considering how well it predicts rainy or cloudy days.
    F1 is the best because it indicates the overall performance of the classification task, providing a balance between precisiona and recall, which is very important
    for scenarios like this one, where both false positives and false negatives are very important and must be accounted for. It is also very good for uneven classes.'''
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1' #BETTER F-MEASURE

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2' #LOWER FPR - SAME TPR

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = '''TPR/FPR is a better measure because it focuses on the ability of the test to correctly identify cancer while minimizing
    false positives , which is something really important in medicine and healthcare. This measure ensures that the test effectively discriminates between actual cancer 
    cases and healthy individuals.'''

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = '''Spam emails. Both false positive and false negatives can be annoying and disruptive for my user, so we only
    really need the system's precision for this type of test.'''
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
