# !python3
# coding: UTF-8


# randomQuiz.py -ランダムに問題と答えを並べて問題集と解答集を作る 
# 詳しい解説はこれを見てね! https://qiita.com/KueharX/items/046d941bf3cd3f7fa675


#問題と選択肢をシャッフルするためにrandomモジュールをインポート。
import random

# 問のデータ。キー（問題部分）と値（答え）を自身で入れ替えることで様々な問題に対応可能

wordQuiz = {'意気':'投合','自業':'自特','天変':'地異','泰然':'自若','魑魅':'魍魎','百花':'繚乱','一挙':'両得','内憂':'外患','破顔':'一笑','右往':'左往','神出':'鬼没','和洋':'折衷','電光':'石火','朝三':'暮四','竜頭':'蛇尾','徹頭':'徹尾'}

# 35通りの問題を作成。range()の中の数字を任意の数字に変えることで何パターン分作るかを決められる。
for quiz_num in range(35):

    #問題集と解答集のファイル作成
    quiz_file = open('randomQuiz{}.txt'.format(quiz_num + 1),'w')
    answer_key_file = open('randomQuiz_answers{}.txt'.format(quiz_num + 1),'w')

    #問題集のヘッダー（名前の記入欄などのスペース）を書く
    quiz_file.write('名前:\n\n日付:\n\n学期:\n\n')
    quiz_file.write((' ' * 28) + '四字熟語クイズ(問題番号{})'.format(quiz_num + 1))
    quiz_file.write('\n\n')

    #言葉の順番をシャッフルする
    Questions = list(wordQuiz.keys())
    random.shuffle(Questions)

    # 問題をループしてそれぞれの問題を作成する
    for question_num in range(len(Questions)):

        #正解と誤答を取得する

        correct_answer = wordQuiz[Questions[question_num]]
        wrong_answers = list(wordQuiz.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers,3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        #問題文と回答選択肢を問題ファイルに書く
        quiz_file.write('{}.{}の後に続く正しい語句は次のうちどれ？\n'.format(question_num + 1,Questions[question_num]))
        for i in range(4):
            quiz_file.write('{}.{}\n'.format('ABCD'[i],answer_options[i]))

        quiz_file.write('\n')

        #答えの選択肢をファイルに書く

        answer_key_file.write('{}.{}\n'.format(question_num + 1,'ABCD'[answer_options.index(correct_answer)]))

    #　ファイルを閉じる
    quiz_file.close()
    answer_key_file.close()
