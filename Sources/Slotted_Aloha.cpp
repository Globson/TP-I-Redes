#include "..//Headers/Slotted_Aloha.hpp"
/*void SlottedAloha(){
  int i,a=1,QuantEstacoes=-1,*Tempo,*Enviado,*Pronto, *Vetor2, TempoAtual=1, Gatilho=0;
  while(QuantEstacoes<1){
    cout<<"Entre com a quantidade de estacoes:";
    cin>>QuantEstacoes;
    if(QuantEstacoes<1){
      cout<<"Valor inválido!"<<endl;
    }
  }
  Tempo = (int*)malloc(QuantEstacoes*sizeof(int));
  Enviado = (int*)malloc(QuantEstacoes*sizeof(int));
  Pronto = (int*)malloc(QuantEstacoes*sizeof(int));
  Vetor2 = (int*)malloc(QuantEstacoes*sizeof(int));
  for(i=0;i<QuantEstacoes;i++){
    Tempo[i]= rand()%10+1;  //Somado com 1 para n poder ser 0;
    Enviado[i]=0;
    Pronto[i]=0; //Inicializando vetores auxiliares.
    cout<<"->  A estacao "<<i+1<<" realizara o envio do seu quadro no tempo: "<<Tempo[i]<<endl;
  }
  int Colisao = 0,Aux=0,Index=0;

  cout<<"\tIniciando tentativas de envio!"<<endl;
  while(Gatilho==0){
    for(i=0;i<QuantEstacoes;i++)
      if(Enviado[i]==0 && TempoAtual==Tempo[i])
        Pronto[i]=1;

    for(i=0;i<QuantEstacoes;i++){
      if(Pronto[i]==1 && Aux==0){
        Aux = 1;
        Vetor2[Index]=i;
        Index++;
      }
      else if(Pronto[i]==1 && Aux ==1){
        Colisao=1;
        Vetor2[Index]=i;
        Index++;
      }
    }
    if(Colisao){
      cout<<"Houve colisão entre as estacoes:"<<endl;
      for(i=0;i<=Index-1;i++){
        Tempo[Vetor2[i]]=Tempo[Vetor2[i]]+a;
        cout<<"\t-> "<<Vetor2[i]+1<<endl;
        a=a*2;
      }
    if(Index>1)
      cout<<endl<<"Os novos tempos para as estacoes que colidiram sao"<<endl;
    for(i=0;i<=Index-1;i++)
      cout<<"Estacao: "<<Vetor2[Index]+1<<" vai enviar em tempo: "<<Tempo[Vetor2[i]]<<endl;
    }
    if(Colisao!=1 && Aux==1){
      Enviado[Vetor2[Index]-1]=1;
      cout<<"A estacao "<<Vetor2[Index-1]+1<< " enviou com sucesso!"<<endl;
      Gatilho=1;
    }
    for(i=0;i<QuantEstacoes;i++){
      if(Enviado[i]==0)
        Gatilho=0;
    }
    for(i=0;i<QuantEstacoes;i++){
      Pronto[i]=0;
    }
    TempoAtual++;
    Colisao=0;
    Aux=0;
    Index=0;

  }

}
*/
void SlottedAloha()
{
  int i,n,k=1,*Tempo,TempoAtual=1,*Enviado,*Pronto,*VetorAux,i1=0,Aux=0,Colisao=0,Gatilho=0;
  system("clear");
  cout<<"O tamanho do frame e de 1 segundo\n\n";
  cout<<"Entre com a quantidade de estacoes:\t";
  cin>>n;
  Tempo=(int*)malloc(n*sizeof(int));
  Pronto=(int*)malloc(n*sizeof(int));
  VetorAux=(int*)malloc(n*sizeof(int));
  Enviado=(int*)malloc(n*sizeof(int));
  for(int i=0; i<n; i++){
	 Tempo[i]=(rand()%10+1);
	 Enviado[i]=0;
   Pronto[i]=0;
	 cout<<"Estacao "<<i+1<<" ira enviar no tempo:  "<<Tempo[i]<<"\n";
  }
  while(Gatilho==0){
  for(i=0; i<n; i++){
	 if(TempoAtual==Tempo[i] && Enviado[i]==0){
		Pronto[i]=1;
	 }
  }
  for(i=0; i<n; i++){
	 if(Pronto[i]==1 && Aux==0){
		Aux=1;
		VetorAux[i1]=i;
		i1++;
    }
	 else if(Pronto[i]==1 && Aux==1){
		Colisao=1;
		VetorAux[i1]=i;
		i1++;
	 }
  }
  if(Colisao==1){
	 cout<<"\nColisao detectada nas estacoes\n";
  for(i=0; i<=i1-1; i++){
	 Tempo[VetorAux[i]]=Tempo[VetorAux[i]]+rand()%10+k;
	 cout<<"\t"<<VetorAux[i]+1;
	 k=k*2;
   }
  if(i1>1)
	 cout<<"\nO novo tempo de envio de cada estacao sera: \t";
  for(i=0; i<=i1-1; i++){
	 cout<<"\nSender "<<VetorAux[i]+1<<" -> "<<Tempo[VetorAux[i]];
    }
  }
  if(Colisao!=1 && Aux==1){
	 Enviado[VetorAux[i1-1]]=1;
	 cout<<"\nA estacao "<<VetorAux[i1-1]+1<<" enviou com sucesso!";
	 Gatilho=1;
  }
  for(i=0; i<n; i++){
	 if(Enviado[i]==0)
		Gatilho=0;
  }
  TempoAtual++;
  for(i=0; i<n; i++){
	 Pronto[i]=0;
  }
  Aux=0;
  Colisao=0;
  i1=0;
  }
}
