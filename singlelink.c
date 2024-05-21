#include<stdio.h>
#include<malloc.h>
#include<process.h>
void create();
void insert_at_beg();
void insert_at_end();
void insert_after_pos();
void del();
void search();
void display();
struct node
{
    int info;
    struct node *link;

}*start=NULL;
int  data, item, n1, pos, i, m;
int main()
{
    int n;
    setbuf(stdout,NULL);
    printf("\n****Linked List*****\n");
    printf("\n1.create\n2.insert at beginning\n3.insert at end\n4.insert after position\n5.delete\n6.search\n7.display\n8.exit\n");
    while(1)
    {
        printf("\nEnter your choice :(1.create 2.insert at Beg. 3.insert at End 4.insert after pos. 5.delete 6.search 7.display 8.exit\n");
        scanf("%d", &n);
        switch(n)
        {
            case 1:
               create();
               break;
            case 2:
               insert_at_beg();
               break;
            case 3:
               insert_at_end();
               break;
            case 4:
                insert_after_pos();
                break;
            case 5:
                del();
                break;
            case 6:
                search();
                break;
            case 7:
                 display();
                 break;
            case 8:
                exit()
            default:
               printf("\nwrong choice !!\n");
        }
    }
    return 0;
}
void create()
{
    struct node *q,  *tmp;
    printf("Enter element :\n");
    scanf("%d", &data);
    tmp=malloc(sizeof(struct node));
     tmp->info=data;
     tmp->link=NULL;
     if(start==NULL)
     start=tmp;
     else
     {
         q=start;
         while(q->link!=NULL)
         q=q->link;
         q->link=tmp;
     }
}
void insert_at_beg()
{
    struct  node *tmp;
    printf("\nEnter the element to be inserted :\n");
    scanf("%d", &data);
    tmp=malloc(sizeof(struct node ));
    tmp->info=data;
    tmp->link=start;
    start=tmp;
    display();
    
}
void insert_at_end()
{
    struct node *tmp, *q;
    printf("\nEnter the element to be inserted  :\n");
    scanf("%d",&data);
    tmp=malloc(sizeof(struct node));
    tmp->info=data;
    tmp->link=NULL;
    if(start==NULL)
    start=tmp;
    else
    {
        q=start;
        while(q->link!=NULL)
        q=q->link;
        q->link=tmp;

    }
    display();

}
void insert_after_pos()
{
    display();
    struct node *q,*tmp;
    int index;
    tmp=malloc(sizeof(struct node));
    
}