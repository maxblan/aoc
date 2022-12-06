#include <stdio.h>  
main()  
{ 
    FILE *fp = fopen("input.txt", "r");
    char str[4096];
    fgets(str, 4096, fp);
    fclose(fp);
    
    for (int i = 0; i < 4096; i++) {
        char temp[14];
        for (int j = 0; j < 14; j++) {
            temp[j] = str[i + j];
        }
        int duplicates = 0;
        for (int k = 0; k < 14; k++) {
            for (int l = 0; l < 14; l++) {
                if (temp[k] == temp[l] && k != l) {
                    duplicates = 1;
                }
            }
        }
        if (duplicates == 0) {
            printf("%d", i + 14);
            break;
        }
    }  
    return 0;
}