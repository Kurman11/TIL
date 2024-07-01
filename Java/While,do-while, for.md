# 반복문 시작

## While문 1
조건식을 확인한다. 참이면 코드 블럭을 실행하고, 거짓이면 while문을 벗어난다.
조건식이 참이면 코드 블럭을 실행한다. 이후에 코드 블럭이 끝나면 다시 조건식 검사로 돌아가서 조건식을 검사한다.(무한 반복)

public class While_3 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;
        int endNum = 3;

        while (i <= endNum){
            sum = sum + i;
            System.out.println("i = "+ i + " sum = "+ sum);
            i++;
        }
    }
}

## do-while문
do-while문은 while문과 비슷하지만, 조건에 상관없이 무조건 한 번은 코드를 실행한다.

public class DoWhile1 {
    public static void main(String[] args) {
        int i = 10;

        do{
            System.out.println("현재 숫자는 :" + i);
            i++;
        } while (i<3);
      }
    }

do-while문은 최초 한번은 항상 실행된다. 따라서 먼저 현재 숫자는:10이 출력된다.
코드 블럭을 실행 후에 조건식을 검증하는데, i = 10이기 때문에 while(i<3)조건식은 거짓이 된다. 따라서 do-while문을 빠져나온다.

## break, continue
break와 continue는 반복문에서 사용할 수 있는 키워드다.
break는 반복문을 즉시 종료하고 나간다. continue는 반복문의 나머지 부분을 건던뛰고 다음 반복으로 진행하는데 사용된다.
참고로 while, do-while, for와 같은 모든 반복문에서 사용할 수 있다.

public class Break1 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        while(true){
            sum = sum + i;
            if (sum >10) {
                System.out.println("합이 10보다 크면 종료 : i=" + i + " sum= " + sum);
                break;
            }
            i++;

        }
      }
    }

    public class Continue1 {
    public static void main(String[] args) {
        int i =1;

        while(i<=5){
            if (i==3){
                i++;
                continue;
            }
            System.out.println(i);
            i++;
        }
    }
}

# for문

public class For2 {
    public static void main(String[] args) {
        int sum =0;
        int endNum = 3;

        for (int i = 1; i <= endNum; i++) {
            sum = sum + i;
            System.out.println("i= "+ i + " sum= " + sum);
        }
    }
}

## for vs while

둘을 비교했을 떄 for문이 더 깔끔하다는 느낌을 받는다. for문은 초기화, 조건 검사, 반복 후 작업 등이 규칙적으로 한 줄에 모두 들어 있어 코드를 이해하기 더 쉽다.

for문

장점 :   
1. 초기화, 조건 체크, 반복 후의 작업을 한 줄에서 처리할 수 있어 편리하다.
2. 정해진 횟수만큼의 반복을 수행하는 경우에 사용하기 적합하다.
3. 루프 변수의 범위가 for 루프 블록에 제한되므로, 다른 곳에서 이 변수를 실수로 변경할 가능성이 적다.

단점 :
1. 루프의 조건이 루프 내부에서 변경되는 경우, for 루프는 관리하기 어렵다.
2. 복잡한 조건을 가진 반복문을 작성하기에는 while문이 더 적합할 수 있다.

while문 

장점 :  
1. 루프의 조건이 루프 내부에서 변경되는 경우, while 로프는 이를 관리하기 쉽다.
2. for 루프보다 더 복잡한 조건과 시나리오에 적합하다.
3. 조건이 충족되는 동안 계속해서 루프를 실행하며, 종료 시점을 명확하게 알 수 없는 경우에 유용하다.

단점 :  
1. 초기화, 조건 체크, 반복 후의 작업이 분산되어 있어 코드를 이해하거나 작성하기 어려울 수 있다.
2. 루프 변수가 while 블록 바깥에서도 접근 가능하므로, 이 변수를 실수로 변경하는 상황이 발생할 수 있다.

한줄로 정리하자면 정해진 횟수만큼 반복을 수행해야 하면 for문을 사용하고 그렇지 않으면 while문을 사용하면 된다. 물론 이것이 항상 정답은 아니니 기준으로 삼는 정도로 이해하자.


