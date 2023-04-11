#include <iostream>
#include <string>
using namespace std;
int charToInt(char& c){
    int intValue = (int)c;
    return intValue-97;
}
char ascii2char(int order){
    int ascii=122-order;
    return (char)ascii;
}
int main(){
    cout<<endl;
    cout<<endl;
    string s2 = "Povzhv hvmw z nvhhztv drgs xfiivmg hvhhrlm rm qhlm ulinzg erz gsrh vcznkov : {\"gbkv\":\"REGISTER\",\"mznv\":\"blfi mznv\",\"hfimznv\":\"blfi hfimznv\",\"vnzro\":\"blfi vnzro zwwivhh\",\"ivtrhgizgrlmKvb\":\"ccc\"}. Kvvk orhgvmrmt mvd nvhhztv uli gzhp xlmgvmg! Ylfi ivtrhgizgrlmKvb : 3u9xvxz6444zx030y85291y54zxyz2u30vzvw4zxw2v8xwuz53xvw1w922596951";
    cout<<" ################################### "<<endl;
    cout<<" With Decrypted registrationKey : "<<endl;
    cout<<" ################################### "<<endl;
    cout<<endl;
    for (char c : s2){
        if ((int)c<97 || (int)c>122){
            cout<<c;
        }
        else{
            int order = charToInt(c);
            c = ascii2char(order);
            cout<<c;
        }
    }
    cout<<endl;
    cout<<endl;
    cout<<" ################################### "<<endl;
    cout<<" With registrationKey given on text: "<<endl;
    cout<<" ################################### "<<endl;
    cout<<endl;
    string s3 = "Povzhv hvmw z nvhhztv drgs xfiivmg hvhhrlm rm qhlm ulinzg erz gsrh vcznkov : {\"gbkv\":\"REGISTER\",\"mznv\":\"blfi mznv\",\"hfimznv\":\"blfi hfimznv\",\"vnzro\":\"blfi vnzro zwwivhh\",\"ivtrhgizgrlmKvb\":\"ccc\"}. Kvvk orhgvmrmt mvd nvhhztv uli gzhp xlmgvmg! Ylfi ivtrhgizgrlmKvb :";
    for (char c : s3){
        if ((int)c<97 || (int)c>122){
            cout<<c;
        }
        else{
            int order = charToInt(c);
            c = ascii2char(order);
            cout<<c;
        }
    }
    cout<<" 3u9xvxz6444zx030y85291y54zxyz2u30vzvw4zxw2v8xwuz53xvw1w922596951"<<endl;
    cout<<endl;
    cout<<endl;
    return 0;
}