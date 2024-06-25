# if, else
파이썬과 비슷

# Switch
public class Switch2 {
    public static void main(String[] args) {
        int grade = 2;

        int coupon;

        switch (grade){
            case 1:
                coupon = 1000;
                break;
            case 2:
                coupon = 2000;
                break;
            case 3:
                coupon = 3000;
                break;
            default:
                coupon = 500;
        }
        System.out.println("발급받은 쿠폰" + coupon);
    }
}
발급받은 쿠폰 2000

파이썬에는 없는 switch문 이지만 if문과 비슷하며 조금만 사용해 봐야겠다.

public class Switch3 {
    public static void main(String[] args) {
        int grade = 2;

        int coupon;

        switch (grade){
            case 1:
                coupon = 1000;
                break;
            case 2:
            case 3:
                coupon = 3000;
                break;
            default:
                coupon = 500;
        }
        System.out.println("발급받은 쿠폰" + coupon);
    }
}
발급받은 쿠폰 3000

만약 break가 없다면 다음 문장으로 이어진다.

## if문 vs switch문
switch문의 조건식을 넣는 부분을 잘 보면 x > 10과 같은 참 거짓의 결과가 나오는 조건이 아니라, 단순히 값만 넣을 수 있다. switch문은 조건신이 특정 case와 같은지만 체크할 수 있다. 쉽게 이야기해서 값이 같은ㅇ지 확인하는 연산만 가능하다.(문자도 가능)  
반면에 if문은 참 거짓의 결과가 나오는 조건식을 자유롭게 적을 수 있다. 예) x >10, x == 10  
정리하자면 swtich문 없이 if문만 사용해도 된다. 하지만 특정 값에 따라 코드를 실행할 때는 switch문을 사용하면 if문보다 간결한 코드를 작성할 수 있다.

### 새로운 switch문
public class Switch4 {
    public static void main(String[] args) {
        int grade = 2;

        int coupon = switch (grade){
            case 1 -> 1000;
            case 2 -> 2000;
            case 3 -> 3000;
            default -> 500;
        };
        System.out.println("발급받은 쿠폰" + coupon);
     }
    }
    

일단 알고만 있자

# 삼항 연산자
if문을 사용할 때 다음과 같이 단순히 참과 거짓에 따라 특정 값을 구하는 경우가 있다.  

```
public class CondOp1 {
    public static void main(String[] args) {
        int age = 18;
        String status;
        if (age >= 18){
            status = "성인";
        } else {
            status = "미성년자";
        }
        System.out.println("age = " + age + " status = " + status );
    }
}
```
위의 코드를 간단히 삼항 연산자를 사용하면
```
public class CondOp2 {
    public static void main(String[] args) {
        int age = 18;
        String status = (age >= 18) ? "성인" : "미성년자";
        System.out.println("age = " + age + " status = " + status );
    }
}
```