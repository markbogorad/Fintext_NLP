# Financial Sentiment Classification with Transformer-Based Models

This project investigates how general-purpose transformer models—specifically DistilBERT—can be adapted to perform sentiment classification on financial text. Through a series of controlled experiments, the study evaluates the impact of different fine-tuning strategies, model configurations, and architectural decisions on performance. Key components include class imbalance correction, custom classification heads, and comparisons with alternative models like FinBERT and BART.

The goal is to understand how far transfer learning can go in closing the performance gap with domain-specific models—while minimizing training cost and complexity.

---

# Table of Contents

1. **Introduction and Objective**

2. **Exploratory Data Analysis (EDA)**

3. **Training Classifier Head Only**
   - 3.1 Experiment 1: Model Preformance Across Varying Subsets ([Subset Fine-Tuning Experiments](./experiments/3.1_subset_finetune.ipynb))
   - 3.2 Experiment 2: Addressing Class Imbalance ([Class Imbalance Experiments](./experiments/3.2_class_imbalance_experiments.ipynb))
   - 3.3 Aside: Working with TFDS - TensorFlow Datasets ([TFDS Demonstration](./experiments/3.3_TFDS_alternative.ipynb))

4. **Supervised Fine-Tuning with Fixed Classifier Head**
   - 4.1 Load Trained Model, Freeze Classifier Head, Unfreeze Encoder

5. **Full Fine-Tuning of Entire Model (Pre-Trained + Classifier Head)**
   - 5.1 Unfreezing
   - 5.2 Experiment 3: Detailed Fine Tuning ([Hyperparameter Fine-Tuning Experiments](./experiments/5.2_full_finetune.ipynb))
   - 5.3 Experiment 4: Fine-Tuning with Custom Head Architecture

6. **Low Rank Adaptation (LoRA)**
   - [LoRA Notebook](./part2_lora_finetune.ipynb)

7. **Evaluating Perfomance on Financial PhraseBank Variants**
   - [Alternate Flavors Experiments](./experiments/7_fin_phrasebank_flavors.ipynb)

8. **Evaluating Alternative Hugging Face Models on Financial PhraseBank**
   - [Alternate HuggingFace Models](./experiments/8_alternate_models.ipynb)

9. **In-Context Learning Experiments**
   - [In-Context Learning Notebook](./experiments/9_in_context_learning_experiments.ipynb)

10. **NLP for Commodities Trading**
    - [#OOTT Sentiment Analysis](../OOTT/oott.ipynb)

11. **Conclusion**

---


## Summary

This repository serves as a modular framework for testing and comparing various adaptation strategies for transformer models in financial NLP. Techniques are extensible to other datasets and domains.

