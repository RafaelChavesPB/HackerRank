#include <bits/stdc++.h>
using namespace std;

typedef struct region_{
    int i_init, j_init, tam;
    string dir;
    region_(int i, int j, string dir){
        this->dir = dir;
        this->init(i,j);
    }
    region_(int dir){
        this->dir = dir;
        this->init(-1,-1);
    }
    void init(int i, int j){
        i_init=i;
        j_init=j;
        tam=1;
    }
    string output(){
        return "I-init: " + to_string(i_init)+"; J-init: " + to_string(j_init)+"; Tam:" + to_string(tam)+ "; Dir: " + dir; 
    }
} region;

vector<region> identifyRegions(vector<string> &grid){
    vector<region> regions;
    for(int i=0; i<10;i++){
        region hor(i,-1,"J");
        for(int j=0; j<=10;j++){
            if(j<10 and grid[i][j]=='-'){
                if(hor.j_init==-1)
                    hor.j_init=j;    
                else
                    hor.tam++;
            }else{
                if(hor.j_init!=-1){
                    if(hor.tam>1)
                        regions.push_back(hor);
                    hor.init(i,-1);
                }
            }
        }
    }

    for(int j=0; j<10;j++){
        region vert(-1,j,"I");
        for(int i=0; i<=10;i++){
            if(i<10 and grid[i][j]=='-'){
                if(vert.i_init==-1)
                    vert.i_init=i;    
                else
                    vert.tam++;
            }else{
                if(vert.i_init!=-1){
                    if(vert.tam>1)
                        regions.push_back(vert);
                    vert.init(-1,j);
                }
            }
        }
    }
    return regions;
}

bool fit(vector<string> &a, region b, string c){
    if(b.tam!=c.size()){
        return false;
    }
    if(b.dir=="I"){
        int tam = b.tam;
        int init = b.i_init;
        int j = b.j_init;
        for(int i=0;i<tam;i++){
            if(a[init+i][j]!='-' and a[init+i][j]!=c[i])
                return false;
        }
    }else if(b.dir=="J"){
        int tam = b.tam;
        int init = b.j_init;
        int i = b.i_init;
        for(int j=0;j<tam;j++){
            if(a[i][init+j]!='-' and a[i][init+j]!=c[j])
                return false;
        }
    }
    return true;
}

vector<string> gridFill(vector<string> a, region b, string c){
    if(b.dir=="I"){
        int tam = b.tam;
        int init = b.i_init;
        int j = b.j_init;
        for(int i=0;i<tam;i++){
            a[init+i][j]=c[i];
        }
    }else if(b.dir=="J"){
        int tam = b.tam;
        int init = b.j_init;
        int i = b.i_init;
        for(int j=0;j<tam;j++){
            a[i][init+j]=c[j];
        }
    }
    return a;
}

vector<string> answer;
void solve(vector<string> grid,vector<string> &words, vector<region> &regions, vector<int> visited, int n){
    if(n==regions.size()){
        answer = grid;
    }
    for(int i=0;i<words.size();i++){
        if(!visited[i] and fit(grid,regions[n],words[i])){
            visited[i]=1;
            solve(gridFill(grid,regions[n],words[i]),words,regions,visited,n+1);
            visited[i]=0;
        }
    }

}

int main(){
    vector<string> grid(10),words;
    vector<region> regions;
    string word;
    for(int i=0;i<10;i++)
        cin>>grid[i];
    cin.ignore();
    while(getline(cin,word,';'))
        words.push_back(word);
    regions = identifyRegions(grid);
    solve(grid,words,regions,vector<int>(words.size(),0),0);
    for(auto x: answer){
        cout<<x<<endl;
    }
}