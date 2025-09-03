from send_request import send_request

def demo_streaming_response():
    print("\n--- Streaming Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.", stream=True)
    print("\n--- End of Streaming Response ---")

def demo_formatted_response():
    print("\n--- Formatted Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.", stream=True, formatted=True)
    print("\n--- End of Formatted Response ---")

def demo_complete_json_response():
    print("\n--- Complete JSON Response ---")
    send_request(model="llama3.1", prompt="Write a haiku.")
    print("\n--- End of Complete JSON Response ---")

# --- Text Classification Demos ---
def demo_text_classification_conversation_1():
    print("\n--- Text Classification: Diagnosis & Scheduling ---")
    conversation = (
        "Patient: I've been having persistent headaches for the past two weeks.\n"
        "Doctor: Have you noticed any other symptoms, such as nausea or vision changes?\n"
        "Patient: Sometimes I feel nauseous, but no vision changes.\n"
        "Doctor: Based on your symptoms, I suspect you may have migraines. Let's schedule an MRI to rule out other causes.\n"
        "Patient: Okay, when can I get the MRI done?\n"
        "Doctor: I'll arrange it for next Monday at 10 AM."
    )
    send_request(model="llama3.1", prompt=f"Classify the following doctor-patient conversation: {conversation}")
    print("\n--- End of Text Classification Demo 1 ---")

def demo_text_classification_conversation_2():
    print("\n--- Text Classification: Medications & DME ---")
    conversation = (
        "My blood sugar has been high lately.\n"
        "Are you taking your insulin as prescribed?\n"
        "I missed a few doses last week.\n"
        "I'll refill your insulin prescription and also order a glucometer for home monitoring.\n"
        "Thank you, I think the glucometer will help."
    )
    send_request(model="llama3.1", prompt=f"Classify the following doctor-patient conversation: {conversation}")
    print("\n--- End of Text Classification Demo 2 ---")

def demo_text_classification_conversation_3():
    print("\n--- Text Classification: Past Medical Conditions ---")
    conversation = (
        "I have a history of asthma and recently I've been coughing a lot.\n"
        "Are you using your inhaler regularly?\n"
        "Yes, but it doesn't seem to help much.\n"
        "I'll review your medication and may adjust your treatment plan based on your asthma history."
    )
    send_request(model="llama3.1", prompt=f"Classify the following doctor-patient conversation: {conversation}")
    print("\n--- End of Text Classification Demo 3 ---")

if __name__ == "__main__":
    print("Demo Script Execution\n")
    
    print("Demo Streaming Response:")
    demo_streaming_response()
    
    print("\nDemo Formatted Response:")
    demo_formatted_response()
    
    print("\nDemo Complete JSON Response:")
    demo_complete_json_response()

    print("\nDemo Text Classification Conversation 1:")
    demo_text_classification_conversation_1()

    print("\nDemo Text Classification Conversation 2:")
    demo_text_classification_conversation_2()

    print("\nDemo Text Classification Conversation 3:")
    demo_text_classification_conversation_3()
