#include <map>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ifstream arquivo;
	arquivo.open("arquivo.txt");
	string palavra;
	map<string,int> mapa;
	if(arquivo.is_open()){
		while(arquivo>>palavra){
			mapa[palavra]=palavra.size();
		}
		for(auto it : mapa){
			cout<<it.first<<' '<<it.second<<endl;
		}
	}else{
		cout<<"Arquivo nao encontrado"<<endl;
	}
}
