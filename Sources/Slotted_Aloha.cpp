#include "..//Headers/Slotted_Aloha.hpp"
void SlottedAloha()
{
  int i,n,k=1,*Tempo,TempoAtual=1,*Enviado,*Pronto,*VetorAux,Index=0,Aux=0,Colisao=0,Gatilho=0;
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
		VetorAux[Index]=i;
		Index++;
    }
	 else if(Pronto[i]==1 && Aux==1){
		Colisao=1;
		VetorAux[Index]=i;
		Index++;
	 }
  }
  if(Colisao==1){
	 cout<<"\nColisao detectada nas estacoes\n";
  for(i=0; i<=Index-1; i++){
	 Tempo[VetorAux[i]]=Tempo[VetorAux[i]]+rand()%k+1;
	 cout<<"\t"<<VetorAux[i]+1;
	 k=k*2;
   }
  if(Index>1)
	 cout<<"\nO novo tempo de envio de cada estacao sera: \t";
  for(i=0; i<=Index-1; i++){
	 cout<<"\nSender "<<VetorAux[i]+1<<" -> "<<Tempo[VetorAux[i]];
    }
  }
  if(Colisao!=1 && Aux==1){
	 Enviado[VetorAux[Index-1]]=1;
	 cout<<"\nA estacao "<<VetorAux[Index-1]+1<<" enviou com sucesso!";
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
  Index=0;
  }
}
