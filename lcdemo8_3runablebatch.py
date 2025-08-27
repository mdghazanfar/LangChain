from langchain_core.runnables import RunnableLambda, RunnableParallel



# batch/abatch: Efficiently transforms multiple inputs into outputs.
# Runnnable lambda - Snippet1
sequence1 = RunnableLambda(lambda x: x + 1) 
result1 = sequence1.invoke(1)
batchresult = sequence1.batch([2,3])  # multiple inputs
print(result1)
print(batchresult)

# Batch: By default, batch runs invoke() in parallel using a thread pool executor

# Async: Methods with “a” suffix are asynchronous. 
# By default, they execute the sync counterpart using asyncio’s thread pool.