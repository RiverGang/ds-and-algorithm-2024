#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(char* shirt_size[], int shirt_size_len) {
    // Write code here.
    int* answer[sizeof(shirt_size_len)];
    for (int i = 0; i < shirt_size_len; i++)
    {
        if (shirt_size[i] = "XS")
            answer[0]++;
        else if (shirt_size[i] = "S")
            answer[1]++;
        else if (shirt_size[i] = "M")
            answer[2]++;
        else if (shirt_size[i] = "L")
            answer[3]++;
        else if (shirt_size[i] = "XL")
            answer[4]++;
        else
            answer[5]++;
    }
    return answer;
}

// The following is main function to output testcase.
int main() {
    char* shirt_size[] = {"XS", "S", "L", "L", "XL", "S"};
    int shirt_size_len = 6;
    int* ret = solution(shirt_size, shirt_size_len);

    // Press Run button to receive output.       
    printf("Solution: return value of the function is {");
    for(int i = 0; i < 6; i++){
        if (i != 0) printf(", ");
        printf("%d", ret[i]);
    }
    printf("} .\n");
}