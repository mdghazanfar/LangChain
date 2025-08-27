from langchain_core.runnables import RunnableLambda, RunnableParallel

# Runnnable lambda - Snippet1
sequence1 = RunnableLambda(lambda x: x + 1) 
result1 = sequence1.invoke(1)
print(result1)

# To perform the below comment snippet1
# A sequence using RunningSequence with RunnableLambda using '|' Pipe operator  - Snippet2
# sequence2 = RunnableLambda(lambda x: x + 1)| RunnableLambda(lambda x: x *4)
# result2 = sequence2.invoke(1) 
# print(result2)

# To perform the below comment snippet2
# A sequence using RunningSequence with RunnableLambda using '|' operator and batch processsing - Snippet3
# RunnableParallel invokes runnables concurrently, providing the same input to each Runnablelambda
# Construct it using a dict literal within a sequence or by passing a dict to RunnableParallel.
# sequence3 = RunnableLambda(lambda x: x + 1) | RunnableParallel({
#     'mulby2': RunnableLambda(lambda x: x * 2),
#     'mulby6': RunnableLambda(lambda x: x * 6)
# })
# result3 = sequence3.invoke(1)
# print(result3)
    