# 연산자

## 산술 연산자

#### 연산자 종류
* 산술 연산자 : +, -, *, /, %(나머지 연산자)
* 증감 연산자 : ++, --
* 비교 연산자 : ==, !=, >, <, >=, <=
* 논리 연산자 : && (AND), || (OR), ! (NOT)
* 대입 연산자 : =, +=, -=, *=, /=, %*
* 삼항 연산자 : ? :

#### 연산자와 피연산자
연산자(operator) : 연산 기호 예) +,-  
피연산자(operand) : 연산 대상 예) 3,4,a,b
        int a = 5, b = 2;
        int sum = a + b;

        // 덧샘
        System.out.println("a + b = " + sum);

        //뺄샘
        int diff = a-b;
        System.out.println("a - b = " + sum);

        // 곱셈
        int multi = a * b ;
        System.out.println("a * b = " + multi);

        // 나눗셈
        int div = a / b;
        System.out.println("a / b = " + div);

        // 나머지
        int mod = a % b;
        System.out.println("a % b = " + mod);

## 연산자 우선순위
#### 연산자 우선순위 암기법
자바는 다음과 같은 연산자 우선순위가 있다. 높은 것에서 낮은 순으로 적었다. 처음에 나오는 괄호()가 우선순위가 가장 높고, 마지막의 대입 연산자(=)가 우선순위가 가장 낮다.

1. 괄호()
2. 단항 연산자 (예 : ++, --, !, ~, new, (type))
3. 산술 연산자 (*, /, % 우선, 그 다음에 +, -)
4. Shift 연산자 (<<, >>, >>>)
5. 비교 연산자 (<,<= >, >=, instanceof )
6. 등식 연산자 (==, !=)\
7. 비트 연산자 (&, ^, |)
8. 논리 연산자 (&&, ||)
9. 삼항 연산자 (? :)
10. 대입 연산자 (=, +=, -=, *=, /=, %= 등등)

#### 애매하면 괄호()를 사용하자

#### 정리
* 연산자 우선순위는 상식선에서 생각하고, 애매하면 괄호를 사용하자
* 누구나 코드를 보고 쉽고 명확하게 이해할 수 있어야한다. 개발자 들이면 연산자 우선순위를 외우고 개발하는 것이 아니다! 복잡하면 명확하게 괄호를 넣어라!
* 개발에서 가장 중요한 것은 단순함과 명확함이다! 애매하거나 복잡하면 안된다.


## 증감 연산자
++와 --로 표현되며, 이들은 변수의 값을 1만큼 증가시키거나 감소시킨다.

#### 전위, 후위 증감연산자
증감 연산자는 피연산자 앞에 두거나 뒤에 둘 수 있으며, 연산자의 위치에 따라 연산이 수행되는 시점이 달라진다.
* ++a : 증감 연산자를 피연산자 앞에 둘 수 있다. 이것을 앞에 있다고해서 전위(Perfix)증감 연산자라 한다.
* a++ : 증감 연산자를 피연산자 뒤에 둘 수 있다. 이것을 뒤에 있다고 해서 후위(Postfix)증감 연산자라 한다.

        // 전위 증감 연산자 사용 예
        int a = 1;
        int b = 0;

        b = ++a; // a의 값을 먼저 증가시키고, 그 결과를 b에 대입
        System.out.println("a = " + a + ", b = " + b);

        // 후위 증감 연산자 사용 예
        a = 1;
        b = 0;

        b = a++; // a의 현재 값을 b에 먼저 대입하고, 그 후 a값을 증가시킴
        System.out.println("a = " + a + ", b = " + b);

## 비교 연산자
비교 연산자는 두 값을 비교하는 데 사용한다. 비교 연산자는 주로 뒤에서 설명하는 조건문과 함께 사용한다.
* == : 동등성 (equal to)
* != : 불일치 (not equal to)
* > : 크다 (greater than)
* < : 작다 (less than)
* >= : 크거나 같다 (greater than or equal to)
* <= : 작거나 같다 (less than or equal to)
비교 연산자를 사용하면 참(true)또는 거짓(false)이라는 결과가 나온다. boolean형을 사용한다.

## 문자열 비교
문자열이 같은지 비교할 때는 ==이 아니라 .equals()메서드를 사용해야 한다.
==를 사용하면 성고할 때도 있지만 실패할 때도 있다.

        String str1 = "문자열1";
        String str2 = "문자열2";

        boolean result1 = "hello".equals("hello"); // 리터럴 비교
        boolean result2 = str1.equals("문자열1"); // 문자열 변수, 리터럴 비교
        boolean result3 = str1.equals("str2"); // 문자열 변수 비교
        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);

        System.out.println("hello" == "hello");

## 논리 연산자
논리 연산자는 boolean형인 true, false를 비교하는데 사용한다.

* && (AND) : 두 피연산자가 모두 참이면 참을 반환, 둘중 하나라도 거짓이면 거짓을 반환
* || (OR) : 두 피연산자 중 하나라도 참이면 참을 반환, 둘다 거짓이면 거짓을 반환
* ! (NOT) : 피연산자의 논리적 부정을 반환. 즉, 참이면 거짓, 거짓이면 참을 반환

        System.out.println("&& : AND 연산");
        System.out.println(true && true);
        System.out.println(true && false);
        System.out.println(false && false);

        System.out.println("|| : OR 연산");
        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || false);

        System.out.println("! 연산");
        System.out.println(!true);
        System.out.println(!false);

        System.out.println("변수 활용");
        boolean a = true;
        boolean b = false;

        System.out.println(a && b);
        System.out.println(a || b);
        System.out.println(!a);
        System.out.println(!b);


## 대입 연산자
축약(복합) 대입 연산자
산술 연산자와 대입 연산자를 한번에 축약해서 사용할 수 있는데, 이것을 축약(복합) 대입 연산자라 한다.
연산자 종류 : +=, -=, *=, /=, %=
