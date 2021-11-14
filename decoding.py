# -*- coding: utf-8 -*-
"""Decoding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0a50jMBAEO6ZDaqimm13RR8rp6nzjBd
"""

! pip install transformers

from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
sequence = ("He began his premiership by forming a five-man war cabinet which included"
            "Chamerlain as Lord President of the Council, Labour leader Clement Attlee as"
            "Lord Privy Seal (later as Deputy Prime Minister), Halifax as Foreign Secretary"
            "and Labour's Arthur Greenwood as a minister without portfolio. In practice,")
inputs = tokenizer.encode(sequence, return_tensors='pt')

outputs = model.generate(inputs, max_length=200, do_sample=True, num_beams=5)
tokenizer.decode(outputs[0])

outputs = model.generate(inputs, max_length=200, do_sample=True, num_beams=5, temperature=1.5)
tokenizer.decode(outputs[0])