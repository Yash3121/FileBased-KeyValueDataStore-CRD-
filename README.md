# File-Based Key-Value DataStore(CRD)! 

# Problem Statement:
- Build a File-Based Key-Value DataStore that supports the basic CRD (Create, Read, and Delete) Operations. This DataStore is meant to be used as local storage for one single process on one laptop. The DataStore must be exposed as a library to clients that can instantiate a class and work with the DataStore.

# Description:
- This Python based Console Application(File-Based Key-Value DataStore) will perform the operations such as `Create, Read and Delete` with `Minimum Space` required which can be stored in the `Local Storage` and also supports the `Thread-Safe operation` and `Time-To-Live property`. I used  `Python's-Threading` concept to ensure that the DataStore to be `Thread-Safe`. Hence, this application will satisfies both the `Functional` and `Non-Functional` requirements. 

# Planning:
- Understanding the Problem Statement.
- Thinking Solution.
- Plan the Coding Structure.
- Coding.
- Documentation.

# Solution(FDS - Functional Dependencies Solved; NFDS - Non-Functional Dependencies Solved):

- [`FDS`]It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
- [`FDS`]A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
- [`FDS`]If Create is invoked for an existing key, an appropriate error must be returned.
- [`FDS`]A Read operation on a key can be performed by providing the key, and receive the value in the response, as a JSON object.
- [`FDS`]A Delete operation can be performed by providing the key.
- [`FDS`]Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.
- [`FDS`]The size of the file storing data must never exceed 1GB.
- [`FDS`]Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must   be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations
- [`FDS`]The client will bear as little memory costs as possible to use this data store while deriving maximum performance with respect to response times for accessing the data store.
    
- [`NFDS`]The size of the file storing data must never exceed 1GB.
- [`NFDS`]More than one client process cannot be allowed to use the same file as a data store at any given time.
- [`NFDS`]A client process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread-safe.
- [`NFDS`]The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store

# Operations Supported:
- [C]Create
- [R]Read
- [D]Delete

# OS in which the project is developed:
- Windows 10

# Language Used:
- Python

# Tools Used:
- VS Code
- Github

                                                                            ***Thank You!***