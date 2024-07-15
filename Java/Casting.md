# 형변환
작은 범위에서 큰 범위로는 당연히 값을 넣을 수 있다.
* int -> long -> double

큰 범위에서 작은 범위는 다음과 같은 문제가 발생할 수있다.
* 소수점 버림
* 오버플로우
```
public class Casting1 {
    public static void main(String[] args) {
        int intValue = 20;
        long longValue;
        double doubleValue;
        
        longValue = intValue;
        System.out.println("longValue = " + longValue);
        
        doubleValue = intValue;
        System.out.println("doubleValue = " + doubleValue);

        doubleValue = 20L;
        System.out.println("doubleValue2 = " + doubleValue);
    }
}
```
* 정리하면 작은 범위에서 큰 범위로의 대입은 자바 언어에서 허용한다. 쉽게 이야기하면 큰 그릇은 작은 그릇에 담긴 내용물을 담을 수 있다.

```
int intValue = 20;

doubleValue = intValue;
doubleValue = (double) intValue // 형 맞추기
doubleValue = (double) 10; // 변수 값 읽기
```
이렇게 앞에 (double)과 같이 적어주면 int형이 double형으로 형이 변한다. 이렇게 형이 변경되는 것을 형변환 이라 한다.
개발자가 이렇게 직접 형변환을 하지 않아도 된다. 이런 과정이 자동으로 일어나기 때문에 ``자동 형변환``, 또는 ``묵시적 형변환``이라 한다.


# 명시적 형변환
``큰 범위에서 작은 범위 대입은 명시적 형변환이 필요하다``
```
    public static void main(String[] args) {
        double doubleValue = 1.5;
        int intValue = 0;

//      intValue = doubleValue;
        intValue = (int) doubleValue;
        System.out.println("intValue = " + intValue);
    }
```
int 형은 double 형보다 숫자의 표현 범위가 작다. 그리고 실수를 표현할 수도 없다. 따라서 이 경우 숫자가 손실되는 문제가 발생할 수 있다.

## 오버플로우
* int로 표현할 수 있는 범위를 넘기면 오버플로우가 발생한다.
* 보통 오버플로우가 발생하면 마치 시계가 한바퀴 돈 것 처럼 다시 처음부터 시작한다. 참고로 -2147483648 숫자는 int의 가장 작은 숫자이다.
* 변수의 타입을 int -> long으로 변경해서 사이즈를 늘리면 오버플로우 문제가 해결된다.
* 오버플로우가 발생하는 것 자체가 문제이다.