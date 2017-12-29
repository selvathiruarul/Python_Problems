def check_cluster(j,zombies,visited):
    for k in range(len(zombies[j])):
        if zombies[j][k]==1 and visited[j][k]==False and visited[j][k]==False:
            visited[j][k]=True
            visited[k][j]=True
            check_cluster(k,zombies,visited)


def zombie(zombies):
    visited = [[False for j in range(len(zombies[i]))]for i in range(len(zombies))]
    print(visited)
    cluster_count=0

    cluster=dict()
    for i in range(len(zombies)):
        flag=False

        for j in range(len(zombies[i])):
            if zombies[i][j]==1 and visited[i][j]==False and visited[j][i]==False:
                visited[i][j]=True
                visited[j][i]=True
                flag=True
                check_cluster(j,zombies,visited)
        if flag:
            cluster_count+=1


if __name__=='__main__':
    zombies=[[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
    print(zombie(zombies))