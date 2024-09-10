# 🙈pokergame
#### 2022 - 1 AI프로그래밍 연습
-------------------------------------------

#### 1. 게임 규칙은 아래와 같습니다.



* 딜러와 플레이어가 각각 2장의 카드를 받음

   - 받은 2장의 카드는 공개함

* 카드를 받으면 플레이어는 Drop 또는 Go를 선택

   - Drop 선택 시 10점*(Go횟수+1)을 잃음

* Go 선택 시 추가로 1장씩을 더 받음

   - 추가로 받는 카드는 상대방에게 공개하지 않음

* 5장을 받았을 때 Go를 선택하면 아래 Poker 규칙에 따라 점수를 계산하여 높은 쪽이 승리

   - 승리할 경우 100점을 얻고 패배할 경우 100점을 잃음

* 만약 점수가 동일하면 점수를 내는 수 (페어 등) 중 가장 큰 수로 결정

   - 모양의 순서는 우열이 없음

  - 그래도 점수가 동일하면 무승부로 점수는 변동 없음    



    
#### 2. 게임에서 점수가 높은 순서는 아래와 같습니다.



* 플러시: 5개의 카드가 모두 같은 모양일 경우

* 스트레이트: 5개의 숫자가 모두 연속일 경우

* 포카드: 4개가 같은 수가 1쌍 있을 경우

* 트리플: 3개가 같은 수가 1쌍 있을 경우

* 2페어: 2개가 같은 수가 2쌍 있을 경우

* 1페어: 2개가 같은 수가 1쌍 있을 경우

* 하이: 위에 해당되지 않는 경우로 가장 큰 수를 갖는 카드로 우열을 정함

* 가진 카드 중 가장 높은 점수에 해당하는 것만으로 우열을 정함



#### 3. 다음과 같은 함수를 사용하여 구현합니다.

   - 필요시 추가로 함수를 정의하여 사용할 수 있습니다.



* 각 점수에 해당하는 지를 확인하는 함수

   - isFlush(cardList) -> high / None

   - isStraight(cardList) -> high / None 

   - is4Cards(cardList) -> high / None

   - isTriple(cardList) -> high / None

   - is2Pairs(cardList) -> high / None

   - is1Pair(cardList) -> high / None

   - isHigh(cardList) -> high / None

* 카드를 정렬하는 함수

   - sortCards(cardList) -> cardList

* 현재 카드 내용을 보여주는 함수

   - viewCards(playerCards) -> cardList

* 카드를 플레이어에게 1장씩 나눠주는 함수

   - handCards(deck, playerCards) -> playerCards



#### 4. 사용할 전역변수는 아래와 같습니다.



* 카드 종류 tuple: SUIT_TUPLE

* 카드 호칭 tuple: RANK_TUPLE

* 초기 점수: INIT_SCORE

* 게임 횟수: MAX_ROUND



#### 5. 사용할 주요 변수 구조 및 예는 아래와 같습니다.



* players = { "dealer", "player" }

* card1 = {'suit': 'Hearts', 'rank': 'Ace', 'value’: 1, ’attr’: ‘hidden’}

* card2 = {'suit': ‘Sapdes', 'rank’: ‘2', 'value’: 2, ’attr’: ‘open’}

* playerCards = { "dealer": cardList, "player": cardList }



### 실행 예시
<pre>
<code>
======================================================================
                    >>> 게임이 시작되었습니다. <<<

>>> dealer 현재 카드 목록입니다. <<<
{'suit': 'Hearts', 'rank': '7', 'value': 7, 'attr': 'open'}
{'suit': 'Hearts', 'rank': '4', 'value': 4, 'attr': 'open'}

>>> player 현재 카드 목록입니다. <<<
{'suit': 'Diamonds', 'rank': 'King', 'value': 13, 'attr': 'open'}
{'suit': 'Clubs', 'rank': '9', 'value': 9, 'attr': 'open'}

>>> 계속 하시겠습니까? 1) Drop, 2) Go ===> 2
>>> 3 번째 카드를 받았습니다 <<<
>>> 계속 하시겠습니까? 1) Drop, 2) Go ===> 2
>>> 4 번째 카드를 받았습니다 <<<
>>> 계속 하시겠습니까? 1) Drop, 2) Go ===> 2
>>> 5 번째 카드를 받았습니다 <<<

>>> dealer 카드 결과는 high 입니다. <<<
{'suit': 'Clubs', 'rank': 'Jack', 'value': 11, 'attr': 'hidden'}
{'suit': 'Spades', 'rank': '8', 'value': 8, 'attr': 'hidden'}
{'suit': 'Hearts', 'rank': '7', 'value': 7, 'attr': 'open'}
{'suit': 'Spades', 'rank': '6', 'value': 6, 'attr': 'hidden'}
{'suit': 'Hearts', 'rank': '4', 'value': 4, 'attr': 'open'}
...

>>> 현재 게임 횟수는 1, 현재 점수는 200 입니다. <<<
>>> 게임을 계속 하시겠습니까? 1) Continue, 2) Stop ===> 2
>>> 게임이 종료되었습니다. <<<
</code>
</pre>
