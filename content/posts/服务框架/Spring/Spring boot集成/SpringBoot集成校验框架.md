---
book_id: 28973507
cnblog_id: '17913109'
doc_id: 92198980
tags:
- 服务框架
- Spring
- Spring boot集成
title: SpringBoot集成校验框架
---
<a name="JUWKn"></a>
# 一、相关规范
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662516179655-9f0b690a-1c86-462a-96ac-4a4d553c012f.png#averageHue=%23f0f0f0&clientId=ued1c3f51-493e-4&errorMessage=unknown%20error&from=paste&height=398&id=uc45e7913&originHeight=796&originWidth=1638&originalType=binary&ratio=1&rotation=0&showTitle=false&size=419582&status=error&style=none&taskId=u74826421-1f9c-4e51-8c6d-8da53ba2c5e&title=&width=819)

- JSR 303 - Bean Validation 1.0
   - 2009年发布
   - 属于JavaEE6的一部分
- JSR 349 - Bean Validation 1.1
   - 2013年发布
   - 属于JavaEE7的一部分
   - 添加方法级验证、错误消息、支持EL表达式等新特性
- JSR 380 - Bean Validation 2.0
   - 2017年8月份完成
   - 属于JavaEE8的一部分
   - 支持容器类型集联验证、添加新的约束注解
<a name="RtZAx"></a>
# 二、Validation 比较
<a name="X1sVG"></a>
## 1、Bean Validation 与Hiberanate Validator

- `Bean Validation` 仅仅是对验证框架定义了规范
- `Hiberanate Validator`是对规范的具体实现
> Bean Validation 1.0参考实现：Hibernate Validator 4.3.1 Final
> Bean Validation 1.1参考实现：Hibernate Validator 5.1.1 Final
> Bean Validation 2.0参考实现：Hibernate Validator 6.0.1 Final

<a name="o1Tkk"></a>
## 2、Hiberanate Validator 与 Spring Validation
`Spring Validation` 在 `Hiberanate Validator` 的基础上，对其进行了二次封装，以满足在Spring环境上更简单、高效的对数据进行验证
<a name="bnEin"></a>
# 三、常用约束注解
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26501265/1662517092686-38e4c0e5-9b26-4fd1-9daf-e88977af0fb0.png#averageHue=%23efefef&clientId=ued1c3f51-493e-4&errorMessage=unknown%20error&from=paste&height=236&id=ufd3f5a45&originHeight=472&originWidth=2016&originalType=binary&ratio=1&rotation=0&showTitle=false&size=255952&status=error&style=none&taskId=u1b2107e0-d694-40cd-8303-9b3ec8b9f79&title=&width=1008)
:::warning
⚠️ **注意**<br />`@NotEmpty` 用在集合类上面<br />`@NotBlank` 用在String上面<br />`@NotNull`  用在基本类型上（"Accepts any type"可以接受任何类型对象）
:::
<a name="aZK0R"></a>
# 四、框架引入
<a name="M0poM"></a>
## 1、依赖
```xml
<!-- Validation 相关依赖 -->
<dependency>
  <groupId>javax.validation</groupId>
  <artifactId>validation-api</artifactId>
  <version>2.0.1.Final</version>
</dependency>
<dependency>
  <groupId>org.hibernate</groupId>
  <artifactId>hibernate-validator</artifactId>
  <version>6.0.16.Final</version>
</dependency>

<!-- Spring Web 自带，可不引入 -->
<dependency>
  <groupId>javax.el</groupId>
  <artifactId>javax.el-api</artifactId>
  <version>3.0.0</version>
</dependency>
```
<a name="E5mYg"></a>
## 2、使用
<a name="YAuGQ"></a>
### 2.1、Field校验
```java
/**
 * 待验证对象实体类
 * 用户信息类
 */
public class UserInfo {

    // 登录场景
    public interface LoginGroup {}

    // 注册场景
    public interface RegisterGroup {}

    // 组排序场景
    @GroupSequence({
            LoginGroup.class,
            RegisterGroup.class,
            Default.class
    })
    public interface Group {}

    /**
     * 用户ID
     */
    @NotNull(message = "用户ID不能为空",
            groups = LoginGroup.class)
    private String userId;

    /**
     * 用户名
     * NotEmpty 不会自动去掉前后空格
     */
    @NotEmpty(message = "用户名称不能为空")
    private String userName;

    /**
     * 用户密码
     * NotBlank 自动去掉字符串前后空格后验证是否为空
     */
    @NotBlank(message = "用户密码不能为空")
    @Length(min = 6, max = 20,
            message = "密码长度不能少于6位，多于20位")
    private String passWord;

    /**
     * 邮箱
     */
    @NotNull(message = "邮箱不能为空",
            groups = RegisterGroup.class)
    @Email(message = "邮箱必须为有效邮箱")
    private String email;

    /**
     * 手机号
     */
    @Phone(message = "手机号不是158后头随便")
    private String phone;

    /**
     * 年龄
     */
    @Min(value = 18, message = "年龄不能小于18岁")
    @Max(value = 60, message = "年龄不能大于60岁")
    private Integer age;

    /**
     * 生日
     */
    @Past(message = "生日不能为未来或当前时间点")
    private Date birthday;

    /**
     * 好友列表
     */
    @Size(min = 1, message = "不能少于1个好友")
    private List<@Valid UserInfo> friends;
}
```
<a name="e5GpA"></a>
### 2.2、接口校验
```java
/**
 * 用户信息服务类
 */
public class UserInfoService {

    /**
     * UserInfo 作为输入参数
     * @param userInfo
     */
    public void setUserInfo(@Valid UserInfo userInfo) {}

    /**
     * UserInfo 作为输出参数
     * @return
     */
    public @Valid UserInfo getUserInfo() {
        return new UserInfo();
    }

    /**
     * 默认构造函数
     */
    public UserInfoService() {}

    /**
     * 接收UserInfo作为参数的构造函数
     * @param userInfo
     */
    public UserInfoService(@Valid UserInfo userInfo) {}

}

```
<a name="copYF"></a>
### 2.3、自定义验证
```java
/**
 * 自定义手机号约束注解
 */
@Documented
// 注解的作用目标
@Target({ElementType.FIELD})
// 注解的保留策略
@Retention(RetentionPolicy.RUNTIME)
// 不同之处：于约束注解关联的验证器
@Constraint(validatedBy = PhoneValidator.class)
public @interface Phone {

    // 约束注解验证时的输出信息
    String message() default "手机号校验错误";

    // 约束注解在验证时所属的组别
    Class<?>[] groups() default {};

    // 约束注解的有效负载
    Class<? extends Payload>[] payload() default {};
}
```
```java
/**
 * 自定义手机号约束注解关联验证器
 */
public class PhoneValidator
        implements ConstraintValidator<Phone, String> {

    /**
     * 自定义校验逻辑方法
     * @param value
     * @param context
     * @return
     */
    @Override
    public boolean isValid(String value,
                           ConstraintValidatorContext context) {

        // 手机号验证规则：158后头随便
        String check = "158\\d{8}";
        Pattern regex = Pattern.compile(check);

        // 空值处理
        String phone = Optional.ofNullable(value).orElse("");
        Matcher matcher = regex.matcher(phone);

        return matcher.matches();
    }
}
```

---

**参考**<br />[告别996 双角度优化编程效率 实现Java高效编程](https://coding.imooc.com/learn/list/382.html)

