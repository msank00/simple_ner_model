# :star: Named-entity-recognizer
Implementation of a `named-entity recognizer` for the English language. The model is trained with a corpus containing almost 14,000 English sentences.  
  
## :dart: Model  
Model (mini model) in the repo is trained using mini data which contains only almost 100 English sentences.  
Therefore, it does not perform well enough.  
  
- I encourage you to train a new model on your own using the corpus in data/ directory.  
- My training lasted almost 20 minutes 
- Training accuracy was 100% where test accuracy was 97%.  
  
## :shield: Usage  

**Training:**

- `python3 src/train.py`

**Inference:**
- `python3  src/predict.py  input-sentence`  
  
### Example

```py  
python3 src/predict.py  "Joe Strummer was born in Ankara."  

# -> Named entity recognizer is loaded.  
# -> [('Joe', 'B-PER'), ('Strummer', 'I-PER'), ('was', 'O'), ('born', 'O'), ('in', 'O'), ('Ankara', 'B-LOC'), ('.', 'O')]
```

  
*P.S. Above example is tested with a model trained on corpus in data/ directory(with almost 14,000 English sentences).*   
  
:rocket: _Happy coding !!_

----

_Simple project template: Use this [link](https://towardsdatascience.com/manage-your-data-science-project-structure-in-early-stage-95f91d4d0600)_

----