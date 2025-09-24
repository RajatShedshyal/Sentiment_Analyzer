### If you only had 200 labeled replies, how would you improve the model without collecting thousands more?  
I would start by using a pre-trained model, fine tune it over these 200 labelled replies. I would use simpler models like Logistic Regression which wont overfit on small datasets and would be able to generalize better. Cross Validation for more good evaluation. I would also use augmentation techinques like (Paraphrasing and Rewording) to get more samples, I did the same in Part A and choosed Logistic Regression Model

### How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?  
I would test the model on various edge cases to catch unwanted behaviour. I would also add safety checks, filters and regular monitoring so that any biased or hamrfull options can be corrected quickly. We could also use a human to cross check the answers. I have done this in my previous project HazardIQ+ where i built a RAG Chatbot and with enoguh edge cases and system prompts i constrained it to handle only Disaster/Help related prompts 

### Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?  
I would make sure that the prompt includes specific details about the person, like thier role, company or recent work. I would also guide the model with clear instrucitons or short examples so the outputs feel personal and not like a generic template. I would run it on various edge test cases to check for unwanted behaviour and fix it. 
