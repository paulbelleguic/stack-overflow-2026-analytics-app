# Cadrage du projet

## Sujet retenu
Thème : **IA**. Sponsor proposé : l'équipe projet de la **DINUM** préparant un pilote d'assistants de code. Il s'agit d'un cas pédagogique, pas d'une commande réelle de cette organisation.

**Question principale : quels usages, outils et besoins de vérification ou de formation la DINUM devrait-elle prioriser pour un premier pilote d'assistants de code ?**

La décision à éclairer est le périmètre d'un pilote : profils à accompagner, outils à examiner, tâches à tester et garde-fous à prévoir. Ce projet ne traite pas la satisfaction au travail ni la fidélisation RH. Il ne mesure pas l'efficacité réelle d'un outil.

## Population commune
- Enquête **2026 seulement** dans la version de départ.
- `Country == "France"` et `CodeMain == "I create code as a primary part of my job"`.
- Une ligne par répondant ; `ResponseId` est unique dans cette édition.
- Archive vérifiée : 30 903 répondants, 794 en France, **628 dans la population retenue**, avant filtres interactifs.
- Toutes industries : ces 628 personnes ne sont pas nécessairement agents publics. Leurs réponses constituent un repère exploratoire, pas une mesure de l'administration française.
- Aucun filtrage sur le fait d'utiliser l'IA : les non-utilisateurs et les réponses manquantes restent visibles dans les effectifs.

## Cinq axes, à approfondir par leurs responsables
| Axe | Question précise | Variables vérifiées |
|---|---|---|
| 1 — Adoption et profils | Comment l'usage déclaré de l'IA varie-t-il selon l'expérience et le rôle ? | `AISelect`, `WorkExp`, `Role`, `Employment` |
| 2 — Outils | Quels assistants de code les répondants ont-ils utilisés et lesquels souhaitent-ils essayer ? | `AICodeAgentHaveWorkedWith`, `AICodeAgentWantToUseNext6Months`, `LLMHaveWorkedWith` |
| 3 — Tâches | Pour quelles tâches les répondants déclarent-ils utiliser l'IA, ou anticipent-ils davantage d'usage ? | `AIWorkCurrentlyUse`, `AIWorkExpectMore`, `AIWorkDoNotPlanToUse` |
| 4 — Vérification | Quelles conditions de confiance et quelles pratiques de vérification sont déclarées ? | `AITrust`, `AIWorkNext`, `AISentiment` |
| 5 — Accompagnement | Comment les répondants apprennent-ils à utiliser l'IA et quels facteurs comptent pour son adoption ? | `LearnAI`, `LearnAIHow`, `AIAdopt` |

## Message du dashboard
Le socle montre des fréquences calculées, puis propose **la vérification des résultats comme point de départ à examiner pour le pilote**. Cette orientation est provisoire : elle doit être confrontée aux explorations des cinq membres et aux besoins réels du sponsor. L'app ne prétend pas avoir identifié un meilleur produit ou démontré un gain de productivité.

## Limites communes
Enquête volontaire, sans pondération représentative de tous les développeurs. Non-réponse et logique conditionnelle du questionnaire ; échantillons réduits après filtres. Les comparaisons sont descriptives, pas causales. Les souhaits d'usage ne sont pas des usages réels, et les réponses multiples ne doivent pas être additionnées comme des personnes différentes.
