# Herança
Digamos que voce tenha criado uma classe Taxas, e para calcular um produto voce precisa realizar certos calculos tributários, porém, embora as taxas se mantenham a mesma, por exemplo: IR, IF, ICMS e etc...
E os cálculos para a mesma também. Elas serão utilizadas em diversas outras classes. Então seria inviável ficar criando
o mesmo atributo para diversas classes.
## É aí que entra herança
Você poderia simplesmente herdar a classe taxas, com os métodos e atributos. E utiliza-los sem ter que ficar criando sempre que criar uma classe nova



# Polimorfismo
Agora usando o exemplo anterior, digamos que você vende um serviço mais complexo que a depender do tipo de produto haverá um cálculo hiperdiferente do comum. Para isso, nós utilizamos o polimorfismo que deixa um ou + métodos agir de maneira diferente... Assim poderiamos alterar por exemplo parametros de calculo de imposto e taxas. Ou até mesmo a forma como eles são realizadas