## Locust常用API
**class HttpLocust(locust)**

- 在Locust类中，具有一个client属性，它对应虚拟用户作为客户端所具备的请求能力，也就是我们常说的请求方法，通常情况下，
我们不会直接使用locust类，因为其client属性没有绑定任何方法。因此在使用locust时，需要先继承locust类，然后在继承子类中的client属性中绑定客户端的实现类；

