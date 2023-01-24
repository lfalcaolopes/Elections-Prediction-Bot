# Bot para prever resultado das eleições de 2022

<li>Projeto tinha como objetivo fazer uma previsão do resultado final do resultado das eleições durante o periodo de apuração dos votos. A análise foi feita por estado
e leva em consideração a porcentagem atual de cada candidato, quantas pessoas já votaram e uma estimativa de quanto seria o total de eleitores que iriam votar, 
estimativa foi feita baseado em quantos eleitores votaram no 1 turno das eleições.</li><br>

<li>Como a apuração oficial não é feita de forma uniforme em todos os estados, acaba sendo apurado os votos dos estados da região sul e sudeste antes da região norte 
e  nordeste, que acaba gerando uma distorção muito grande na porcentagem de votos para cada candidato no estagio inicial da apuração, já que as regiões sul e sudeste, 
em sua maioria, são mais propensas a votar em Bolsonaro e as regiões norte e nordeste mais propensas a votar no Lula.</li><br>

<li>O projeto então entra para tentar minimizar essa distorção, fazendo uma estimativa de quantos votos cada cadidato irá receber, caso a porcentagem de votos 
em cada estado se mantenha até o final da apuração dos votos, o que o torna mais preciso com o passar da apuração.</li><br>

<li>O código foi executado diversas vezes durante a apuração para ver como ele se comportaria em cada estágio da apuração. Após o fim, o programa não acertou 
precisamente a porcentagem de votos dos candidatos, como era esperado já que foram feitas estimativas do total de eleitores, foi interessante perceber que durante 
todo o processo ele apontou o candidato Lula como o vencedor, mesmo quando a apuração oficial marcava uma boa vantagem de votos para o candidato Bolsonaro.</li><br>
</ul>

## Imagens de cada estagio da apuração
<table align="center">
  <tr>
    <td>20% da apuração</td>
    <td>30% da apuração</td>
    <td>40% da apuração</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/61370784/214142834-6963f9a8-043d-4743-ae19-3554e9f09dc1.jpeg" width="500"  ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214142848-a389f4b2-ddff-4abe-ad08-2ba5d508e733.jpeg" width="500"  ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214142887-85c54414-157a-4403-8c65-be092e063fdc.jpeg" width="500" ></td>
  </tr>
 </table>

<table align="center">
  <tr>
    <td>50% da apuração</td>
    <td>60% da apuração</td>
    <td>75% da apuração</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143146-fe22e972-1342-4c22-80b1-19345bc2ac5e.jpeg" width="500" ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143160-14235f17-965c-4f83-83d9-54ff9b09ff6f.jpeg" width="500" ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143167-1a549c22-fb5a-45bf-983b-747074d31ec9.jpeg" width="500" ></td>
  </tr>
 </table>

 <table align="center">
  <tr>
    <td>85% da apuração</td>
    <td>90% da apuração</td>
    <td>95% da apuração</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143172-10449e7d-8c1d-429c-aeb5-044bd3f965ef.jpeg" width="500" ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143172-10449e7d-8c1d-429c-aeb5-044bd3f965ef.jpeg" width="500" ></td>
    <td><img src="https://user-images.githubusercontent.com/61370784/214143196-0410a064-9b0a-4072-a6cb-902621957750.jpeg" width="500" ></td>
  </tr>
 </table>
 
 ## Gráfico da apuração oficial
 <p align="center">
  <img src="https://user-images.githubusercontent.com/61370784/214148503-98441ae7-7d46-4a6f-8f89-454b818cfe47.png" width="500"  >
 </p>
