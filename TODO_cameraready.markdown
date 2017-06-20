## Premier reviewer

- [ ] if 140 runs are needed to get some decent results - how can the approach work based on wet-lab studies, where often only 3 "runs" exist? 
- [ ] In the conclusion it is mentioned that in the future it is planned to investigate the applicability of these methods to real experiments. But is this not the point? We do not need PAC do analyse simulation traces (because in these cases we already have the model), we need methods that allow us to derive models based on real experiments. Here at least an indication under which circumstances the approach will work for real experiments should be provided (also this discussion is announced in the abstract). 

- [ ] So far the performance of PAC has not been compared with other methods yet.  Here it would be interesting to discuss in more detail the possible benefit that PAC would have, given its focus on influence models, and particularly in combination with background knowledge, because also other learning approaches improve significantly when given some knowledge that can be exploited for constraining the search space of hypotheses. 

## Deuxième reviewer

- [ ] The title does not seem to reflect the content of the paper. The title is very generic while the content is mainly restricted to specific paradigms. 

- [ ] "Automating the process", mentioned in the Abstract, does not appear in the text.

- [ ] Many quantitative adjectives are used but are not supported by any theoretical or empirical results. Some examples: "fully readable", "more or less readable", "very poor results", "particularly relevant", "straightforwardly represented", "low-end laptop". 

- [ ] It is not clear to me how the quasi-linear number of Boolean activation sample per species is guaranteed. 

- [ ] The methodology of a building k-CNF formula equivalent to an influence system could be better explained. 
Section 3 is lacking formal proofs (or references). E.g., 
    - Influence systems and k-CNF formulae equivalence. 
    - Why monotone DNF cannot encode the Boolean dynamics of influence systems with negation? 
    
- [ ] The notation is not always clear. I propose the Biocham v4 notation to be explained in the paper, otherwise it is almost impossible to follow all the examples and listings. 

- [ ] Empirical results on learning the T-lymphocyte model could have been better presented. The learning parameters, e.g., L,h, are not given; the comparison metrics are not clear; and the explanations of the two cases, with and without prior knowledge, are not satisfactory. 

- [ ] The limitations with respect to realistic experiments, promised in the abstract, are finally not discussed. 

- [ ] Many grammatical and/or syntactical mistakes that reduce readability, e.g., we mean not that, uniformize, experimentation, were run.

## Troisième Reviewer

- [ ] this is a curiosity: can the model structure learned as a boolean network be lifted to a quantitative model, e.g. somehow reversing the construction from Tomas networks, but learning parameters by parameter estimation methods? Can you comment on this? 
- [ ] I like the expression “shortage of available models”… Do you think these learning techniques can be made fully automatic and do not require a model to supervise them? 
- [ ] When you discuss about active learning in the introduction, maybe you can also cite and discuss the paper [a] (cf end of the review), which uses active learning for model identification in a logic based framework. 
- [ ] Section 2.1. I think introduction partial and complete boolean vectors, but not using the former further on is a useless complication. Please rewrite this section introducing only total vectors (and call them vectors). If you really feel you need it, a remark at the end of the section mentioning partial ones will do.
- [ ] Section 2.2. What is a prime implicant? 
- [ ] Section 3.1. What is the meaning of a target vector? What do you mean with the notation x \sigma t? It in not introduced, particularly in a boolean context. Please define it (I suspect it is and or or of the vectors). 
- [ ] Section 3.4. Is example 6, referring to a model not introduced, really needed here? It’s a bit disturbing as a forward pointer. 
- [x] Section 4.2, page 9. You mean (b) rather than (c)?
- [ ] Section 4.2. What is the impact on the framework (from a mathematical viewpoint) of the imperfect oracle assumption?
- [ ] Page 12. Listing 5 is in an unfortunate position. 
- [ ] Section 4.4. It seems that the issue about pathways A and B is an an issue about rare events. If we do not observe them, your  framework will miss them. This is not surprising, yet this may be a drawback of trying to learn an exact model from a incomplete information set. Any chance of using Bayesian learning to account for this uncertainty in a principles way? Can you discuss about this? 
- [ ] Page 14. Figure 4 is in the appendix, but mentioned in the text. How will you deal with this in the final version, given the page limits?

## Arthur

- [ ] Replacer les figures citées dans le texte dans le corps du papeir et pas en annexe.
