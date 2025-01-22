import random as rand
randnum=[]

def refilllist():
 '''It resets the list used to pick random numbers for question picking from a pool upon change in question pool'''
 global randnum
 randnum=[1,2,3,4,5,6,7,8,9,10]

def randomquestionpicker():
    '''It return a unique random integer b/w 1 to 10 which is then used to choose a question from a pool of 10 questions, it is unique as every time an integer is choosen it is delleted from the list and the list is reseted using refillist() when the pool is changed'''
    global randnum
    randompop=(rand.choice(randnum))
    randnum.remove(randompop)  # print(randnum) # print(randompop)
    return randompop

def answer_ranomasier(anslst=[]):
    '''It take a list consisting of four possible answers and radomize them so every time the options are presented the correct answer will not be on the same place'''
    answerrandomlist=[1,2,3,4]
    finalanswerlist=[]
    for i in range(4):
        answerpop=rand.choice(answerrandomlist)
        answerrandomlist.remove(answerpop)
        if answerpop==1:finalanswerlist.append(anslst[1])
        elif answerpop==2:finalanswerlist.append(anslst[2])
        elif answerpop==3:finalanswerlist.append(anslst[3])
        elif answerpop==4:finalanswerlist.append(anslst[4])
    return finalanswerlist


def question_answers1to5():
    '''It returns questions from a pool of six question and its multiple options out of which only one is correct.It is only used when user is on Question no. 1 to 5 hence contain easy difficulty questions'''
    i=randomquestionpicker()
    match i:
        case 1:
            q1='Who wrote India\'s National Anthem?'
            finalanswerlist=[q1,'RK Narayan','Chetan Bhagat','Lal Bahadur Shastri','Rabindranath Tagore']
            return finalanswerlist
        
        case 2:
            q1='Which city is known as the Pink City of India?'
            finalanswerlist=[q1,'Kochi','Maysore','Banglore','Jaipur']
            return finalanswerlist
        
        case 3:
            q1='How many major religions are there in India?'
            finalanswerlist=[q1,'8','4','5','6']
            return finalanswerlist

        case 4:
            q1='When is the National Hindi Diwas celebrated?'
            finalanswerlist=[q1,'15 August','13 September','14 July','14 September']
            return finalanswerlist

        case 5:
            q1='Which country is the largest producer of coffee in the world?'
            finalanswerlist=[q1,'Colombia','Vietnam','Ethiopia','Brazil']
            return finalanswerlist

        case 6:
            q1='Who wrote Vande Mataram?'
            finalanswerlist=[q1,'Rabindranath Tagore','Sarat Chandra Chattopadhyay','Ishwar Chandra Vidyasagar','Bankim Chandra Chatterjee']
            return finalanswerlist

        case 7:
            q1='Which one of the following places is famous for the Great Vishnu Temple?'
            finalanswerlist=[q1,'Bamiyan, Afghanistan','Panja Sahib, Pakistan','Bordubar, Indonesia','Ankorvat, Cambodia']
            return finalanswerlist
        
        case 8:
            q1='Where is the largest Buddhist Monastery in India located?'
            finalanswerlist=[q1,'Gangtok, Sikkim','harmashala, Himachal Pradesh','Sarnath, Uttar Pradesh','Tawang, Arunachal Pradesh']
            return finalanswerlist

        case 9:
            q1='Which of the following administrative innovations during the Mughal Empire had the most significant long-term impact on the empire\'s revenue collection system?'
            finalanswerlist=[q1,'Introduction of the Mansabdari system','Implementation of Akbar\'s Dahsala system','Creation of the Diwan-i-Arz','Establishment of the Jagirdari system']
            return finalanswerlist

        case 10:
            q1='Who was the first Indian woman to win a medal in the Olympics?'
            finalanswerlist=[q1,'Bachendri Pal','Kunjarani Devi','P.T. Usha','Karnam Maleshwari']
            return finalanswerlist

def question_answers6to8():
    '''It returns questions from a pool of six question and its multiple options out of which only one is correct.It is only used when user is on Question no. 6 to 8 hence contain medium difficulty questions'''
    i=randomquestionpicker()
    while i>6:
        i=randomquestionpicker()
    match i:
        case 1:
            q1='Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?'
            finalanswerlist=[q1,'India Gate','Qutub Minar','Charminar','Vijay Stambha']
            return finalanswerlist
        
        case 2:
            q1='Which ancient civilization is credited with the invention of the first known writing system, cuneiform?'
            finalanswerlist=[q1,'Greeks','Egyptians','Romans','Sumerians']
            return finalanswerlist
        
        case 3:
            q1='Which Mughal Emperor was deported to Rangoon by the British?'
            finalanswerlist=[q1,'Bahadur Shah I','Akbar Shah I','Shah Jahan','Bahadur Shah II']
            return finalanswerlist

        case 4:
            q1='Which administrative reform implemented by Alauddin Khalji during the Delhi Sultanate was most crucial in maintaining the stability of his empire?'
            finalanswerlist=[q1,'Introduction of the iqtadari system','Establishment of the Diwan-i-Risalat','Formation of the Mansabdari system','Implementation of market control policies']
            return finalanswerlist

        case 5:
            q1='The fine step-well complex of \'Agrasen ki Baoli\' is located at'
            finalanswerlist=[q1,'Agra','Gwalior','Amritsar','New Delhi']
            return finalanswerlist

        case 6:
            q1='The National Stadium in Delhi was earlier known by the name'
            finalanswerlist=[q1,'Mountbatten Stadium','Wellington Stadium','Canning Stadium','Irwin Stadium']
            return finalanswerlist

def question_answers9to11():
    '''It returns questions from a pool of six question and its multiple options out of which only one is correct.It is only used when user is on Question no. 9 to 11 hence contain Hard difficulty questions'''
    i=randomquestionpicker()
    while i>6:
        i=randomquestionpicker()
    match i:
        case 1:
            q1='Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?'
            finalanswerlist=[q1,'Solicitor General','Cabinet Secretary','Chief Justice','Attorney General']
            return finalanswerlist
        
        case 2:
            q1='Who, in 1978, became the first person to be born in the continent of Antarctica?'
            finalanswerlist=[q1,'James Weddell','Nathaniel Palmer','Charles Wilkes','Emilio Palma']
            return finalanswerlist
        
        case 3:
            q1='Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868?'
            finalanswerlist=[q1,'Belgium','Italy','France','Denmark']
            return finalanswerlist

        case 4:
            q1='Leena Gade, a person of Indian origin, is the first female race engineer to win which of the following races?'
            finalanswerlist=[q1,'Indianapolis 500','24 Hours of Le Man','12 Hours of Sebring','Monaco Grand Prix']
            return finalanswerlist

        case 5:
            q1='Who is the first woman to successfully climb K2, the world’s second highest mountain peak?'
            finalanswerlist=[q1,'Junko Tabei','Tamae Watanabe','Chantal Mauduit','Wanda Rutkiewicz']
            return finalanswerlist

        case 6:
            q1='Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?'
            finalanswerlist=[q1,'Mir Taqi Mir','Mohammad Ibrahim Zauq','Abul-Qasim Ferdowsi','Zahir Dehlvi']
            return finalanswerlist

def question_answers12():
    '''It returns questions from a pool of six question and its multiple options out of which only one is correct.It is only used when user is on Question no. 12 hence contain Extremely Hard difficulty questions'''
    i=randomquestionpicker()
    while i>6:
        i=randomquestionpicker()
    match i:
        case 1:
            q1='The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla?'
            finalanswerlist=[q1,'Viceregal Lodge','Gorton Castle','Cecil Hotel','Barnes Court ']
            return finalanswerlist
        
        case 2:
            q1='Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?'
            finalanswerlist=[q1,'Fort Canning Park','National University of Singapore','National Gallery of Singapore','Cathay Cinema Hall']
            return finalanswerlist
        
        case 3:
            q1='Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk?'
            finalanswerlist=[q1,'Asanga','Mahadharmarakshita','Dharmaraksita','Nagasena']
            return finalanswerlist

        case 4:
            q1='What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?'
            finalanswerlist=[q1,' The Want and Means of India','National Dividend of India','The Law and Lawyers','The Problem of the Rupee']
            return finalanswerlist

        case 5:
            q1='According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer\'s curse?'
            finalanswerlist=[q1,'Kshemadhurti','Dharmadatta','Mitadhvaja','Prabhanjana']
            return finalanswerlist

        case 6:
            q1='Which was the first mountain peak above 8,000 metres in height to be summited by humans?'
            finalanswerlist=[q1,'Lhotse','Kanchenjunga','Makalu','Annapurna']
            return finalanswerlist


def q1to5(m):
    '''It combines the results for Question no. 1 to 5 from different methods and present user with question and its multiple choices placed at different location each time and then verify weather the answer user has given is right or not if its right it tells the ammount of money he has won and if its wrong it shows Wrong Answer'''
    
    match m:
        case 1:money=1000
        case 2:money=5000
        case 3:money=25000
        case 4:money=75000
        case 5:money=150000
    
    question_answer_return=question_answers1to5()
    question_answer_return=list(question_answer_return)
    question=question_answer_return[0]
    
    returned_random_answers=answer_ranomasier(question_answer_return)
    returned_random_answers=list(returned_random_answers)
    
    a=returned_random_answers[0]
    b=returned_random_answers[1]
    c=returned_random_answers[2]
    d=returned_random_answers[3]

    print(f'{question}')
    print(f'A.{a}\nB.{b}\nC.{c}\nD.{d}')
    print()
    useranswer=input('Your answer is: ')
    if useranswer=='a' and a==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='b' and b==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='c' and c==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='d' and d==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    else:
        print('Wrong Answer')
        print('GAME OVER')
        ret='Wrong'
        return ret
    print()

def q6to8(m):
    '''It combines the results for Question no. 6 to 8 from different methods and present user with question and its multiple choices placed at different location each time and then verify weather the answer user has given is right or not if its right it tells the ammount of money he has won and if its wrong it shows Wrong Answer'''
    match m:
        case 6:money=300000
        case 7:money=600000
        case 8:money=1200000
    
    question_answer_return=question_answers6to8()
    question_answer_return=list(question_answer_return)
    question=question_answer_return[0]
    
    returned_random_answers=answer_ranomasier(question_answer_return)
    returned_random_answers=list(returned_random_answers)
    
    a=returned_random_answers[0]
    b=returned_random_answers[1]
    c=returned_random_answers[2]
    d=returned_random_answers[3]

    print(f'{question}')
    print(f'A.{a}\nB.{b}\nC.{c}\nD.{d}')
    print()
    useranswer=input('Your answer is: ')
    if useranswer=='a' and a==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='b' and b==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='c' and c==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='d' and d==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    else:
        print('Wrong Answer')
        print('GAME OVER')
        ret='Wrong'
        return ret
    print()

def q9to11(m):
    '''It combines the results for Question no. 9 to 11 from different methods and present user with question and its multiple choices placed at different location each time and then verify weather the answer user has given is right or not if its right it tells the ammount of money he has won and if its wrong it shows Wrong Answer'''
    match m:
        case 9:money=2400000
        case 10:money=4800000
        case 11:money=9600000
    
    question_answer_return=question_answers9to11()
    question_answer_return=list(question_answer_return)
    question=question_answer_return[0]
    
    returned_random_answers=answer_ranomasier(question_answer_return)
    returned_random_answers=list(returned_random_answers)
    
    a=returned_random_answers[0]
    b=returned_random_answers[1]
    c=returned_random_answers[2]
    d=returned_random_answers[3]

    print(f'{question}')
    print(f'A.{a}\nB.{b}\nC.{c}\nD.{d}')
    print()
    useranswer=input('Your answer is: ')
    if useranswer=='a' and a==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='b' and b==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='c' and c==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='d' and d==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    else:
        print('Wrong Answer')
        print('GAME OVER')
        ret='Wrong'
        return ret
    print()

def q12(m):
    '''It combines the results for Question no. 12 from different methods and present user with question and its multiple choices placed at different location each time and then verify weather the answer user has given is right or not if its right it tells the ammount of money he has won and if its wrong it shows Wrong Answer'''
    match m:
        case 12:money=15000000
    
    question_answer_return=question_answers12()
    question_answer_return=list(question_answer_return)
    question=question_answer_return[0]
    
    returned_random_answers=answer_ranomasier(question_answer_return)
    returned_random_answers=list(returned_random_answers)
    
    a=returned_random_answers[0]
    b=returned_random_answers[1]
    c=returned_random_answers[2]
    d=returned_random_answers[3]

    print(f'{question}')
    print(f'A.{a}\nB.{b}\nC.{c}\nD.{d}')
    print()
    useranswer=input('Your answer is: ')
    if useranswer=='a' and a==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='b' and b==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='c' and c==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    elif useranswer=='d' and d==question_answer_return[4]:print(f'Congrates you have won {money} rs')
    else:
        print('Wrong Answer')
        print('GAME OVER')
        ret='Wrong'
        return ret
    ret='YOU WON'
    print(ret)
    return ret
    print()


def main():
 while True:
  wanttoplay=(input('Do you wish to play Yes(1)/No(anything): '))
  if wanttoplay!='1':
      print('By')
      break
  elif wanttoplay=='1':
     while True:
      for i in range(12):
        if (i+1)<=5:
            print(i+1)
            if i+1==1:refilllist()
            check=q1to5(i+1)
            if check=='Wrong':break
        elif (i+1)>5 and (i+1)<9:
            print(i+1)
            if i+1==6:refilllist()
            check=q6to8(i+1)
            if check=='Wrong' or i+1==12:break
        elif (i+1)>8 and (i+1)<12:
            print(i+1)
            if i+1==9:refilllist()
            check=q9to11(i+1)
            if check=='Wrong' or i+1==12:break
        else:
            print(i+1)
            check=q12(i+1)
            if i+1==12 or check=='Wrong':break
      if check=='YOU WON' or check=='Wrong' or i==12:break

if __name__==('__main__'):
    main()
