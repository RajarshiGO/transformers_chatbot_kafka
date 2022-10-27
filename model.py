from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
#nb_sentences = 1

tokenizer = torch.load("tokenizer.pt")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None
prev_response = None
def chatbot(msg):
    global chat_history_ids
    global prev_response
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(
        msg + tokenizer.eos_token, return_tensors="pt"
    )
    # append the new user input tokens to the chat history
    bot_input_ids = (
        torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        if chat_history_ids is not None
        else new_user_input_ids
    )
    #print(chat_history_ids.size() if chat_history_ids is not None else "first")
    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )
    # pretty print last ouput tokens from bot
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
    )
    if(response == prev_response):
        bot_input_ids = new_user_input_ids
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1] :][0], skip_special_tokens=True
        )

    prev_response = response
    return response