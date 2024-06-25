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

