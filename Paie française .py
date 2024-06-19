1.Cotisation assurance maladie maternité invalidité décès 

Les cotisations de Sécurité sociale
Au 1er janvier 2019, une nouvelle réglementation fait baisser le taux d'assurance maladie de 13 % à 7 % '
pour les employeurs éligibles à ce qu'on appelle la "réduction générale", '
pour les salariés dont la rémunération n'excède pas 2,5 Smic à l'année, en cumulé. 
Lorsqu'on parle d'un calcul "à l'année" ou encore "en cumulé", "au cumul", cela signifie qu'il faut calculer les montants concernés '
et les comparer depuis le 1er janvier de l'année, au mois de paie en cours. '


Exemple :  

Un salarié perçoit une rémunération brute de 3 500 € en janvier 2020, 4 500 € en février 2020 et 3 800 € en mars 2020.

Sa rémunération brute cumulée est donc de 11 800 €. 

Pour vérifier si on applique un taux de 7 % ou 13 % au titre de l'assurance maladie, on va donc comparer ce montant avec 2,5 Smic cumulés.'

Soit (1 539,42 * 3) * 2,5 = 11 545,65 €.

11 800 > 11 545,65 La rémunération brute cumulée est supérieure à 2,5 SMIC cumulés, donc on applique un taux de 13 % depuis le 1er janvier 2020. 

Cela signifie entre autres que si la rémunération passe en dessous le mois suivant, on devra régulariser le taux (de 13 % à 7 %), 
depuis le 1er janvier 2020 également. Donc, pour un salarié donc la rémunération brute varie beaucoup d'un mois sur l'autre, 
cela peut être synonyme de régularisations conséquentes d'un mois à l'autre. 

1.Cotisation assurance maladie maternité invalidité décès : 
Est-ce que le salaire brut est supérieur à 2,5 SMIC (sur une base annuelle cumulée,
donc de janvier au mois de paie calculé) ? Si oui, on applique un taux de 13 %, sinon de 7 %.


###=>>>> Dévloppé par DAH ###=> Employeur sur Totalité du salaire

###=>>>>>2,5 SMIC=> SMIC+payslip.SMIC  sur une base annuelle cumulée,donc de janvier au mois de paie calculé

cumul SMIC =>  result =SMIC+payslip.SMIC 


###=>>>>>BRUT
result = salaire brut (y compris les heures supplémentaires)
+primes et indemnités +prestations sociales complémentaires
+revenus de remplacement en cas d'arrêt maladie, maternité ou accident de travail (C’est ce qu’on appelle le maintien de salaire)'
+prestations familiales extralégales+avantages en espèces servis par le comité d'entreprise'
+avantages en nature (nourriture et logement, mise à disposition de voiture pour l'usage privé des salariés, etc.)'

-Certains éléments ne sont pas soumis à cotisations :

-indemnités journalières versées par la Sécurité sociale  'IJSS' => nettes
-primes liées à l’intéressement des salariés aux résultats de l’entreprise
-gratifications versées à l’occasion de la remise de la médaille d’honneur du travail, dans la limite du salaire mensuel de base
-indemnités considérées comme des dommages et intérêts
-primes liées à la participation des salariés aux résultats de l’entreprise, lorsqu’elles sont versées dans le cadre d’un accord collectif
-frais professionnels et frais d'entreprise pouvant être justifiés'

Prenons un exemple : un salarié perçoit une rémunération mensuelle brute de 2 500 euros.
Au cours du mois de mars, ce salarié est en arrêt maladie. Sa rémunération brute est diminuée de 258 euros en raison de cette absence.
Son revenu de remplacement lié à cette absence est de 130 euros bruts, et est versé par l’entreprise. C’est ce qu’on appelle le maintien de salaire. 
Enfin, les IJSS brutes de la Sécurité sociale s'élèvent à 110 euros, et seront prélevées sur le bulletin de paie.'

Pour le mois de mars, quel sera le salaire brut de notre salarié ?
Salaire de base : 2 500 euros.
Absence maladie : – 258 euros.
Maintien de salaire : + 130 euros.
IJSS brutes : – 110 euros.

Salaire brut de mars : 2 262 euros.


Dans certains cas, la base des cotisations est différente du montant des rémunérations brutes (CSG-CRDS, forfait social, base forfaitaire). 
Nous aurons l'occasion de le voir plus en détail dans le chapitre suivant.'

La base de calcul des cotisations ne peut jamais être inférieure à la rémunération minimale légale, le Smic, ou à la rémunération conventionnelle.
###=>>>> Dévloppé par DAH ###=> Employeur sur Totalité du salaire
###=>>>>>cumul_BRUT=> BRUT+payslip.BRUT    sur une base annuelle cumulée,donc de janvier au mois de paie calculé
cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
cumul_RS = cumul_RS1 + cumul_RS2
cumul_BRUT => result =BRUT+payslip.BRUT 
cumul_SMIC => result =SMIC+payslip.SMIC 
cumul_PMSS => result =PMSS+payslip.PMSS
cumul_T1 => result =T1+payslip.cumul_T1
cumul_T2 => result =T2+payslip.cumul_T2
payslip.nbr_payslip

assurance.maladie

a = cumul_BRUT
d = cumul_RS
b = cumul_SMIC
c = payslip.cumul_assurance.maladie

if (a+d)> 2.5*b: 
    result=(a+d)*0.13-c or ( T1 + T2) * 0.13 -c
else:  
    result=(a+d)*0.07-c or ( T1 + T2) * 0.07 -c

###=>>>> Dévloppé par DAH
cumul_assurance.maladie => result=assurance.maladie+payslip.cumul_assurance.maladie

(1) En Alsace-Moselle, une cotisation salariale maladie est due au taux de 1,50% 

Assurance.maladie ###=>Salarié sur Totalité du salaire
result =(T1+T2)*0.0015    #BRUT*0.0015

(1) Pour les non-résidents une cotisation salariale maladie est due au taux de 5,50 % (CSS art. L 131-9 et D 242-3). cas détachement ou Impartiation
Assurance.maladie ###=>Salarié sur Totalité du salaire
result =(T1+T2)*0.0055       #BRUT*0.0055

###=>>>> Dévloppé par DAH 
- Contribution de solidarité autonomie (CSA) ###=>Employeur sur Totalité du salaire
result =(T1+T2)* 0.003     # BRUT*0.003

###=>>>> Dévloppé par DAH 

    Périodes    Salaires mensuels   Salaires cumulés    PMSS    PMSS cumulés    Tranche 1   Tranche 2   
    Janvier           3100              3100            3428        3428          3100        
    Février           3100              6200            3428        6856          3100        
    Mars              3100              9300            3428      10 284          3100        
    Avril             3100            12 400            3428      13 712          3100        
    Mai               3100            15 500            3428      17 140          3100        
    Juin  3100+2300 = 5400            20 900            3428      20 568          5068        332 
    Juillet           3100            24 000            3428      23 996          3428       -328    
    Août              3100            27 100            3428      27 424          3104         -4  
    Septembre         3100            30 200            3428      30 852          3100        
    Octobre           3100            33 300            3428      34 280          3100        
    Novembre          3100            36 400            3428      37 708          3100        
 Décembre 3100+3100 = 6200            42 600            3428      41 136          4736       1464    

                                261 000,00          41 136,00   267 384,00      41 136,00    1 464,00   


Si le cumul des salaires est > au cumul PMSS, alors
la tranche 1 = cumul PMSS – base cotisations tranche 1 précédentes cumulées.
La tranche 2 = cumul des salaires – cumul PMSS – bases cotisations tranche 2 précédentes.

Si le cumul des salaires est < au cumul PMSS, alors
la tranche 1 = cumul salaire – base cotisations tranche 1 précédentes cumulées.
la tranche 2 =  – base cotisations tranche 2 précédentes cumulées.

T1 = cumul PMSS – base cotisations tranche 1 précédentes cumulées.
 4 736,00   
T2 =cumul des salaires - cumul PMSS – bases cotisations tranche 2 précédentes. 
 1 464,00   
T1 =cumul salaire – base cotisations tranche 1 précédentes cumulées. 
 3 100,00 

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2  

SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS
cumul_T1 => result =T1+payslip.cumul_T1
cumul_T2 => result =T2+payslip.cumul_T2

T1
if SC+RS<SP:
    result= cumul salaire + cumul_RS – base cotisations tranche 1 précédentes cumulées. => cumul_BRUT + cumul_RS - payslip.cumul_T1
else:  
    result = cumul PMSS – base cotisations tranche 1 précédentes cumulées.   => cumul_PMSS - payslip.cumul_T1

T2
if SC+RS>SP:
    result = cumul des salaires + cumul_RS – cumul PMSS – bases cotisations tranche 2 précédentes. => cumul_BRUT + cumul_RS - cumul_PMSS - payslip.cumul_T2
else: 
    result =  – base cotisations tranche 2 précédentes cumulées.                        =>   - payslip.cumul_T2       #Vérifié   


###=>>>> Dévloppé par DAH 
Assurance vieillesse déplafonnée ###=>Employeur sur Totalité du salaire
if cumul_BRUT + cumul_RS > 1 cumul_PMSS:
    result = (T1+T2)*0.019
else:  
    result=0
Assurance vieillesse déplafonnée ###=>Salarié sur Totalité du salaire
if cumul_BRUT + cumul_RS > 1 cumul_PMSS:
    result = (T1+T2)*0.004 
else:  
    result=0
    
Assurance vieillesse plafonnée ###=>Employeur sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;
###=>>>>cumul_PMSS => result = PMSS+payslip.PMSS
#cumul_assurance.vieillesse_plafonnée => result=assurance.vieillesse_plafonnée +payslip.cumul_assurance.vieillesse_plafonnée 

#T1 result= cumul salaire - base cotisations tranche 1 précédentes cumulées.

# if cumul_BRUT> 1 cumul_PMSS 
#     result =(T1)*0.0855
# else:  
result=(T1)*0.0855

Assurance vieillesse plafonnée ###=>Salarié sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;

# if cumul_BRUT> 1 cumul_PMSS 
#     result =(T1)*0.069
# else:  
result=(T1)*0.069

###=>>>> Dévloppé par DAH

# if cumul_BRUT>4 cumul_PMSS :  
#     result = 4 cumul_PMSS*0,0405 - payslip.cumul_assurance.chômage
# else:  
#     result= cumul_BRUT*0,0405 - payslip.cumul_assurance.chômage

- Assurance chômage    T1      Employeur sur Salaire limité à 4 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €  TA à 1 P  & TB à 4 P

cumul_assurance.chômage T1 => result=assurance.chômage T1+payslip.cumul_assurance.chômage T1

Assurance chômage T1  

result = T1*(0.0405)   

(3) Pour les intermittents du spectacle, une contribution patronale et une contribution salariale additionnelles sont dues 
afin de financer le régime spécifique à cette profession.

Pour les CDD d’usage d’au plus 3 mois conclus avec un intermittent du spectacle ou un ouvrier docker occasionnel, 
la contribution patronale chômage est majorée de 0,50 %.

Assurance chômage T1  

result = T1*(0.0405+0.0050)   

# if(cumul_BRUT>=4 cumul_PMSS ):  
#     result = 4 cumul_PMSS*(0,0405+0.0050) - payslip.cumul_assurance.chômage
# else:  
#     result=(T1)*(0,0405+0.0050)

#if(0<BRUT <1):  
    #result = BRUT*(0,0405+0.0050)  
#elif(1<=BRUT <4): 
    #result = 1 P*(0,0405+0.0050)    
#elif(4<=BRUT):  
    #result = 4 P*(0,0405+0.0050)   
#else:  
    #result=0 

- Assurance chômage   T2       Employeur sur Salaire limité à 4 P  >2020: PMSS tranche 2 (4 P) : de 3 428 € à 13 712 €.

#if(1 cumul_PMSS<cumul_BRUT <=4 cumul_PMSS): 
# result = (T2)*0,0405 
#else:  
    #result=0 

#if BRUT> 1 P 
    #result=(BRUT-PMSS tranche 1 P)*0,0405  ainsi de suite
#else:  
    #result=0

cumul_assurance.chômage T1 => result=assurance.chômage T1+payslip.cumul_assurance.chômage T1
cumul_assurance.chômage T2 => result=assurance.chômage T2+payslip.cumul_assurance.chômage T2

Si le cumul des salaires est > au 4 cumul PMSS, alors
4P1 = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées.
Si le cumul des salaires est < au 4  cumul PMSS, alors
4P1 = cumul salaire  – base cotisations 4 P1 précédentes cumulées.

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2  

SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS

4 PMSS cumulés = 4 * SP

cumul_4 P1 => result =4 P1+payslip.4 P1

4 P1
if SC + RS < 4*SP:
    result= cumul salaire + cumul_RS – base cotisations 4 P1 précédentes cumulées. => cumul_BRUT + cumul_RS - payslip.4 P1
else:  
    result = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées. => 4 * SP - payslip.4 P1

Assurance chômage T2  

if (SC + RS) < 4*SP:
    result = (SC + RS)*(0.0405)-cumul_assurance.chômage T1-payslip.cumul_assurance.chômage T2  or result = (4 P1-T1) * 0.0405
else
    result = 4*SP*(0.0405)-cumul_assurance.chômage T1-payslip.cumul_assurance.chômage T2 or result = (4 P1-T1) * 0.0405


Pour les CDD d’usage d’au plus 3 mois conclus avec un intermittent du spectacle ou un ouvrier docker occasionnel, 
la contribution patronale chômage est majorée de 0,50 %.

Assurance chômage T2 

if (SC + RS)< 4*SP:
    result = (SC + RS)*(0.0405+0.0050)-cumul_assurance.chômage T1-payslip.cumul_assurance.chômage T2   or result = (4 P1-T1) * (0.0405+0.0050)
else
    result = 4*SP*(0.0405+0.0050)-cumul_assurance.chômage T1-payslip.cumul_assurance.chômage T2 or result = (4 P1-T1) * (0.0405+0.0050)


#if(1 cumul_PMSS<cumul_BRUT <=4 cumul_PMSS): 
# result = (T2)*(0,0405+0.0050) 
#else:  
    #result=0 

#if(0<BRUT <=1):
    #result = 0  
#elif(1<BRUT <4): 
    # result = (BRUT-PMSS tranche 1 P)*(0,0405+0.0050) 
#elif(4<=BRUT):  
    #result = 0 #(PMSS tranche 2)*(0,0405+0.0050) 
#else:  
    #result=0 


- Assurance chômage  AGS        Employeur sur Salaire limité à 4 P  >2020:  de 0 € à 13 712 €.
dans la limite de 13 712 € (correspondant à la tranche A + la tranche B4).

cumul_AGS  => result=AGS+payslip.AGS

Assurance chômage AGS

Si le cumul des salaires est > au 4 cumul PMSS, alors
4P1 = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées.
Si le cumul des salaires est < au 4  cumul PMSS, alors
4P1 = cumul salaire – base cotisations 4 P1 précédentes cumulées.

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2  

SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS

4 PMSS cumulés = 4 * SP

cumul_4 P1 => result =4 P1+payslip.4 P1

4 P1
if (SC + RS)< 4*SP:
    result= cumul salaire + cumul_RS – base cotisations 4 P1 précédentes cumulées. => cumul_BRUT + cumul_RS - payslip.4 P1
else:  
    result = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées. => 4 * SP - payslip.4 P1

result = 4 P1*0.0015 

# if(cumul_BRUT>=4 cumul_PMSS ):  
#     result = 4 cumul_PMSS*(0.0015) - payslip.cumul_assurance.chômageAGS
# else:  
#     result= =((T1)+(T2))*0.0015 = BRUT*0.0015 #(cumul_BRUT)*(0.0015) - payslip.cumul_assurance.chômageAGS

# if BRUT>= 4 P =13 712
#     result=4 P*0.0015
# else:  
#     result=BRUT*0.0015

mais il descend à 0,03 % pour le personnel intérimaire des entreprises de travail temporaire.
(4) Les entreprises de travail temporaire sont soumises pour le personnel intérimaire à un taux de cotisation AGS spécifique de 0,03%.

result = 4 P1*0.0003

# if(cumul_BRUT>=4 cumul_PMSS ):  
#     result = 4 cumul_PMSS*(0.0003) - payslip.cumul_assurance.chômageAGS
# else:  
#     result= ((T1)+(T2))*0.0003= BRUT*0.0003 # (cumul_BRUT)*(0.0003) - payslip.cumul_assurance.chômageAGS

#if BRUT>= 4 P =13 712
    #result=4 P*0.0003
#else:  
    #result=BRUT*0.0003


2.Contribution allocations familiales : est-ce que le salaire brut est supérieur à 3,5 SMIC 
(sur une base annuelle cumulée, donc de janvier au mois de paie calculé) ?
Si oui, on applique un taux de 3,45 % ainsi qu'un taux additionnel de 1,80 %'
sinon on applique seulement un taux de 3,45 %.
##=>>>> Dévloppé par DAH ###=> Employeur sur Totalité du salaire "déplafonnée"
###=>>>>>3,5 SMIC=> SMIC+payslip.SMIC  sur une base annuelle cumulée,donc de janvier au mois de paie calculé

Cumul SMIC  result =SMIC+payslip.SMIC 
*payslip.nbr_payslip

###=>>>>>cumul_BRUT=> BRUT+payslip.BRUT  sur une base annuelle cumulée,donc de janvier au mois de paie calculé
cumul_BRUT => result =BRUT+payslip.BRUT 

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2 

allocations familiales CAF
cumul_CAF => result =CAF+payslip.cumul_CAF

a = cumul_BRUT
d = cumul_RS
b = cumul_SMIC
c = payslip.cumul_CAF

if (a+d) > 3.5*b:
    result=(a+d)*(0.00345+0.0018)-c   or ( T1 + T2) * (0.00345+0.0018) -c #(0.00345+0.0018)=0.0525 
else:  
    result=(a+d)*0.00345-c            or ( T1 + T2) * 0.00345 -c 


###=>>>> Dévloppé par DAH
Le versement au Fonds national d'aide au logement (Fnal)'

- Cotisation FNAL plafonnée ###=>Employeur sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;
un taux de 0,10 %, limité au plafond de la Sécurité sociale pour les employeurs ayant moins de 50 salariés "plafonnée"
Depuis le 1er janvier 2020, si vous avez dépassé le seuil de 50 salariés, 
il faut vérifier si le seuil est toujours dépassé pendant 5 années consécutives, 
avant d'appliquer le taux de 0,50 %. Si l'entreprise repasse en-dessous du seuil, alors le taux de 0,50 % ne lui sera plus applicable, et ainsi de suite.

if Total nombre id employee= ETP < 50   categorie_id A créer un champ et se base sur total des employés Actif 
ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (T1)*0.001
else:  
    result=0

- Cotisation FNAL déplafonnée ###=>Employeur sur Totalité du salaire

un taux de 0,50 % sur la totalité des rémunérations pour les employeurs ayant plus de 50 salariés. "déplafonnée"
L'effectif qui détermine le taux et l'assiette de la contribution correspond 
à la moyenne du nombre de personnes employées au cours de chacun des mois de l'année civile précédente.' = > Effectif moyen
if Total nombre id employee ETP >= 50  categorie_id A créer un champ et se base sur total des employés Actif 
ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (T1+T2)*0.005  #BRUT*0.005  
else:  
    result=0
  
Depuis le 1er janvier 2020, si vous avez dépassé le seuil de 50 salariés, 
il faut vérifier si le seuil est toujours dépassé pendant 5 années consécutives, avant d'appliquer le taux de 0,50 %. '
Si l'entreprise repasse en-dessous du seuil, alors le taux de 0,50 % ne lui sera plus applicable, et ainsi de suite.'

controle = payslip.regul_seuil_categorie_id = le seuil est toujours dépassé pendant 5 années consécutives
a=Total nombre id employee ETP
if controle:
    if a>=50:  
        result=(T1+T2)*0.005
    else:  
        result=(T1)*0.001

MODE DE CALCUL DE L'EFFECTIF MOYEN EN SE BASANT DE L'ANNEE CIVILES PREEDENTES?
ASSIETTE DE COTISATIONS ?

Les cotisations de retraite complémentaire obligatoire :

tranche 1 : de 0 € à 3 428 € ;

tranche 2 : de 3 428 € à 27 424 €.

La complémentaire : Cotisation de base sur T1

Cotisation de base sur T1 ###=>Employeur sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;
#if cumul_BRUT> 1 cumul_PMSS
    #result =0
#else:  
result=(T1)*0.0472

Cotisation de base sur T1 ###=>Salarié sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;

#if cumul_BRUT> 1 cumul_PMSS
    #result =0
#else:  
result=(T1)*0.0315

La complémentaire :CEG sur T1

CEG sur T1 ###=>Employeur sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;
#if cumul_BRUT> 1 cumul_PMSS
    #result =0
#else:  
result = (T1)*0.0129

CEG sur T1 ###=>Salarié sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;

#if BRUT> 1 P 
    #result =0
#else:  
result=(T1)*0.0086

La complémentaire : Cotisation de base sur T2

Cotisation de base sur T2 ###=>Employeur sur Salaire entre 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €. ; result = ( 8 P1 - T1 )*0.1295
result = ( 8 P1 - T1 )*0.1295

Si le cumul des salaires est > au 8 cumul PMSS, alors
8P1 = 8 cumul PMSS – base cotisations 8 P1 précédentes cumulées.
Si le cumul des salaires est < au 8  cumul PMSS, alors
8P1 = cumul salaire – base cotisations 8 P1 précédentes cumulées.

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2 

SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS

8 PMSS cumulés = 8 * SP

cumul_8 P1 => result =8 P1+payslip.8 P1

8 P1
if SC + RS < 8*SP:
    result= cumul salaire + cumul_RS – base cotisations 8 P1 précédentes cumulées. => cumul_BRUT + cumul_RS - payslip.8 P1
else:  
    result = 8 cumul PMSS – base cotisations 8 P1 précédentes cumulées. => 8 * SP - payslip.8 P1 

# if cumul_BRUT>= 8 cumul_PMSS:  
#     result = 8 cumul_PMSS*(0.1295) - payslip.cumul_complémentaire.Cop de base sur T2
# else
#     result = (T2)*0.1295 

#if(1<BRUT <8): 
    #result = (T2)*0.1295 
#elif(8<=BRUT):  
    #result = 8 cumul_PMSS*(0.1295) - payslip.cumul_complémentaire.Cop de base sur T2
#else:  
    #result=0 
 

Cotisation de base sur T2 ###=>Salarié sur sur Salaire entre 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €.  ;
result = ( 8 P1 - T1 )*0.0864

# if cumul_BRUT>= 8 cumul_PMSS:  
#     result = 8 cumul_PMSS*(0.0864) - payslip.cumul_complémentaire.Cos de base sur T2
# else
#     result = (T2)*0.0864

# if(1<cumul_BRUT <8): 
#     result = (T2)*0.0864
# elif(8<=cumul_BRUT):  
#     result = 8 cumul_PMSS*(0.0864) - payslip.cumul_complémentaire.cos de base sur T2
# else:  
#     result=0 

# if(1<BRUT <8): 
#     result = (BRUT-PMSS tranche 1 P)*0.0864
# elif(8<=BRUT):  
#     result = 8 P*0.0864   #(8 PMSS tranche 2)*0.0864
# else:  
#     result=0 

La complémentaire : CEG sur T2

CEG sur T2 ###=>Employeur sur Salaire entre 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €. ;
result = ( 8 P1 - T1 )*0.0162
# if cumul_BRUT>= 8 cumul_PMSS:  
#     result = 8 cumul_PMSS*(0.0162) - payslip.cumul_CEG Cop sur T2
# else
#     result = (T2)*0.0162

#if(1<cumul_BRUT <8): 
    #result = (T2)*0.0162
#elif(8<=cumul_BRUT):  
    #result = 8 cumul_PMSS*(0.0162 ) - payslip.cumul_CEG Cop sur T2
#else:  
    #result=0 
  
#elif(1<BRUT <8): 
    #result = (BRUT-PMSS tranche 1 P)*0.0162
#elif(8<=BRUT):  
    #result = 8 P*0.0162  #(8 PMSS tranche 2)*0.0162 
#else:  
    #result=0 

CEG sur T2 ###=>Salarié sur sur Salaire entre 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €.  ;
result = ( 8 P1 - T1 )*0.0108
# if cumul_BRUT>= 8 cumul_PMSS:  
#     result = 8 cumul_PMSS*(0.0108) - payslip.cumul_CEG Cos sur T2
# else
#     result = (T2)*0.0108

#if(1<cumul_BRUT <8): 
    # result = (T2)*0.0108
#elif(8<=cumul_BRUT):  
    #result = 8 cumul_PMSS*(0.0108) - payslip.cumul_CEG Cos sur T2 
#else:  
    #result=0 

#if(1<BRUT <8): 
    #result = (BRUT-PMSS tranche 1 P)*0.0108
#elif(8<=BRUT):  
    #result = 8 P*0.0108   #(8 PMSS tranche 2)*0.0108
#else:  
    #result=0 
     
La CEG est très souvent cumulée sur le bulletin de salaire avec la cotisation de retraite complémentaire, 
ce qui donne les taux suivants répartis par tranche :
- Sécurité sociale plafonnée   
Tranche 1 : 4,01 % part salariale et 6,01 % part patronale.
- Sécurité sociale déplafonnée      
Tranche 2 : 9,72 % part salariale et 14,57 % part patronale.

La CET Contribution d'équilibre technique : est-ce que le salaire est supérieur au 1 PMSS (sur une base annuelle cumulée, donc de janvier au mois de paie calculé) ?'
Si oui, alors on applique le calcul de la cotisation depuis le début. Sinon, on ne la calcule pas sur le bulletin. 

La CET (uniquement si rémunération supérieure à 1 P) Salaire limité à 8 P ###=>Employeur sur Salaire entre 1 P+1 et 8 P >>>2020: PMSS tranche 2 : de 3 429 € à 27 424 €

CET
Une nouvelle CET (Contribution d’équilibre technique) est créée. Elle s’applique à tous les salariés dont le salaire est supérieur au  1 plafond de la Sécurité sociale. Pour ces personnes, 
la CET est prélevée sur les tranches 1 et 2 au taux de 0,35 %.

 	 
        CET Assiette Tranche 1 + Tranche 2
Part salariale              	Part patronale	            Total
Taux	0,14%	                   0,21%	                0,35%

Salaires mensuels = (T1)+(T2)

###=>>>> Dévloppé par DAH   

if(SC < 1 SP;0;SI(SC > 1 SP;cumul 8P1-payslip CET précedents))

cumul_CET.COP => result=CET.COP+payslip.cumul_CET.COP
# a = cumul_BRUT
# b = cumul_PMSS
# c = payslip.cumul_CET.COP

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
RS = cumul_RS = cumul_RS1 + cumul_RS2 


SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS


8 PMSS cumulés = 8 * SP

cumul_8 P1 => result =8 P1+payslip.8 P1
cumul_CET => result=CET+payslip.cumul_CET

Base CET  #if(SC<1 SP ;0;SI(SC>1 SP;cumul 8P1-payslip CET précedents))

if SC + RS  > SP:
    result = cumul_8 P1 - payslip.cumul_CET 
else :
    result = 0

CET.COP  ###=>>>> Dévloppé par DAH 

if SC + RS > SP:
    result = Base CET*0.0021
else:
    result = 0

or result = Base CET*0.0021

# a = cumul_BRUT
# b = cumul_PMSS
# c = payslip.cumul_CET.COP

# if(0<= a <=1):
#     result = 0 
# elif a >= 8 cumul_PMSS:
                                
#     result= 8 cumul_PMSS*0.0021-c
# else:  
#     result=a*0.0021-c        

#if(0<=BRUT <=1):
    #result = 0 
#elif BRUT>= 8 P = 27 424
    #result= 8 P*0.0021
#else:  
    #result=BRUT*0.0021

La CET (uniquement si rémunération supérieure à 1 P) Salaire limité à 8 P ###=>Salarié sur Salaire entre 1 P+1 et 8 P >>>2020: PMSS tranche 2 : de 3 429 € à 27 424 €

###=>>>> Dévloppé par DAH
cumul_CET.COS => result=CET.COS+payslip.cumul_CET.COS


CET.COS  ###=>>>> Dévloppé par DAH 

if SC + RS > SP:
    result = Base CET*0.0014
else:
    result = 0
or  result = Base CET*0.0014

# a = cumul_BRUT
# b = cumul_PMSS
# c = payslip.cumul_CET.COS

# if(0<= a <=1):
#     result = 0 
# elif a >= 8 cumul_PMSS:
                                
#     result= 8 cumul_PMSS*0.0014-c
# else:  
#     result=a*0.0014-c


#if(0<=BRUT <=1):
    #result = 0 
#elif BRUT>= 8 P = 27 424
    #result= 8 P*0.0014
#else:  
    #result=BRUT*0.0014

###=>>>> Dévloppé par DAH
L' Apec :'
Cotisation APEC : est-ce que le salarié dépend des articles 4 et 4bis de la convention collective nationale de 1947 ?  Cadres=categorie_id (statut de cotisant "cadre" ou "assimilé cadre")
Si oui, on calcule la cotisation sur le bulletin tous les mois. 
les salariés avec un statut de cotisant "cadre" ou "assimilé cadre", 
c'est-à-dire qui cotisent au titre des articles 4 et 4 bis de la Convention collective nationale de 1947.'

APEC
 	   APEC (pour les salariés cadres)    tranches A et B       Salaire limité à 4 P
            Assiette Tranche 1 + Tranche 2 limitée à 4 fois le plafond de la sécurité sociale
     Part salariale              	      Part patronale	            Total
Taux	0,024%	                              0,036%	                0,06%

Salaires mensuels = (T1)+(T2)= BRUT

categorie_id A  un champ hr.employee

APEC ###=> Employeur sur Salaire limité à 4 P  >2020:  de 0 € à 13 712 €.dans la limite de 13 712 € (correspondant à la tranche A + la tranche B4). tranches A et B  Salaire limité à 4 P

RS = cumul_RS = cumul_RS1 + cumul_RS2 

cumul_APEC.COP => result=APEC +payslip.cumul_APEC.COP
SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS
cumul_4 P1 => result =4 P1+payslip.4 P1

4 PMSS cumulés = 4 * SP


if employee.categorie_id=='Cadre' 
    result = 4 P1*0.00036
else: 
    result=0
# if employee.categorie_id=='Cadre' and (cumul_BRUT>=4 cumul_PMSS ):
#     result = 4 cumul_PMSS*(0.00036) - payslip.cumul_APEC.COP
# elif employee.categorie_id=='Cadre' and (cumul_BRUT <4 cumul_PMSS ):
# else:  
#     result= ((cumul_BRUT)*(0.00036) - payslip.cumul_APEC.COP) #BRUT*0.00036
# else: 
#     result=0

APEC ###=>###=>###=>Salarié sur Salaire limité à 4 P  >2020: PMSS tranche 2 (4 P) : de 3 428 € à 13 712 €.dans la limite de 13 712 € (correspondant à la tranche A + la tranche B)

if employee.categorie_id=='Cadre' 

    result = 4 P1*0.00024
else: 
    result=0
#cumul_APEC.COS => result=APEC +payslip.cumul_APEC.COS
# if employee.categorie_id=='Cadre' and (cumul_BRUT>=4 cumul_PMSS ):
#     result = 4 cumul_PMSS*(0.00024) - payslip.cumul_APEC.COS
# elif employee.categorie_id=='Cadre' and (cumul_BRUT <4 cumul_PMSS ):
#     result=((cumul_BRUT)*(0.00024) - payslip.cumul_APEC.COS) #BRUT*(0.00024)
# else: 
#     result=0

###=>>>> Dévloppé par DAH
Assurance décès obligatoire  ###=>###=>    Salaire limité à 1 P  

est-ce que le salarié dépend des articles 4 et 4bis de la convention collective nationale de 1947 ?  Cadres=categorie_id (statut de cotisant "cadre" ou "assimilé cadre")
Si oui, on calcule la cotisation sur le bulletin tous les mois. 
les salariés avec un statut de cotisant "cadre" ou "assimilé cadre"   

Assurance décès obligatoire ###=>Employeur sur Salaire limité à 1 P >>>2020: PMSS tranche 1 : de 0 € à 3 428 € ;

if employee.categorie_id=='Cadre' # and (cumul_BRUT <>= 1 cumul_PMSS )and (cumul_BRUT > 1 cumul_PMSS ):
    result =(T1)*0.0150
else:  
    result=0

###=>>>> Dévloppé par DAH ###Accident du travail, maladies professionnelles => Employeur sur Totalité du salaire  
L’assiette de cotisation d’accident de travail est calculée sur le salaire déplafonné, c’est-à-dire sur le salaire total brut.
Les cotisations d'accidents du travail'
Cette cotisation concerne les risques suivants :accidents du travail ; maladies professionnelles ; accidents du trajet.
Le taux de cette cotisation est fixé par la Caisse d'assurance retraite et de la santé au travail (Carsat), '
en fonction des risques encourus par les salariés au sein de l'entreprise.'
Plus la taille de l’entreprise augmente, plus le taux est individualisé et repose sur les résultats de l’établissement en matière de sécurité. 
Selon l’activité et la taille de l’entreprise, le taux notifié est : 

un taux dit collectif ou national ;
un taux mixte ;
un taux individuel.

result =((T1)+(T2))*0.Tx COP

###=>>>> Dévloppé par DAH 
- Financement des organisations syndicales ou Contribution au dialogue social ###=>>>> Dévloppé par DAH =>  Employeur sur Totalité du salaire  
Une contribution patronale permet de financer la mise en place d'un fonds paritaire dédié '
au financement des organisations syndicales de salariés et des organisations professionnelles d'employeurs. '
Il s'agit de la contribution au dialogue social.'

result =((T1)+(T2))*0.00016 #= BRUT*0.00016
###=>>>> Dévloppé par DAH
Versement mobilité => ###=>>>> Dévloppé par DAH Employeur sur Totalité du salaire

Le versement mobilité (VM) succède au versement transport (VT). 

C'est une contribution due par tous les employeurs qui embauchent plus de 10 salariés. '
Elle permet de financer les transports en commun.Vous devez la payer à l'Urssaf, '
qui la reverse ensuite aux autorités organisatrices de transports (AOT) locales.
Le versement transport (pour les employeurs de plus de 11 salariés dans un périmètre de transport urbain)
Il s'agit d'une contribution locale des entreprises au financement des transports publics.

Tout employeur public ou privé à partir de 11 salariés, dont l'établissement est situé dans un périmètre de transport urbain, '
doit cotiser au versement transport :

en région parisienne ;

dans le périmètre d'une autorité organisatrice de transport (AOT).'

Ne cotisent pas au versement transport :

les fondations et associations reconnues d'utilité publique à but non lucratif et à caractère social ;'

les représentants d'États étrangers et certains organismes internationaux.'

Salariés comptabilisés : L'effectif de l'entreprise est évalué au 1er janvier de l'année précédente.Au total du 01/01/N-1'

Il doit correspondre à la moyenne des effectifs déterminés chaque mois de l'année civile (tous établissements confondus dans une même zone de transport).'

À noter : certains contrats ne sont pas pris en compte dans les effectifs. 
Il s'agit des salariés en CDD qui remplacent une personne absente, '
des apprentis, des contrats d'accompagnement dans l'emploi.

L'effectif englobe tous les salariés ayant un contrat de travail le dernier jour de chaque mois (y compris les salariés absents).'

if Total nombre id employee ETP > 10   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'
    #result = (BRUT)*TX VM    TX VM=Taux AOT  => result = ((T1)+(T2))*TX VM 
    result = result = ((T1)+(T2))*TX VM   TX VM=Taux AOT
else:  
    result=0

Calcul du taux de versement mobilité transport (Simulateur)

Permet de connaître le taux de versement mobilité applicable dans la ville où est situé votre établissement.
L'Urssaf propose un outil de calcul de votre contribution qui donne accès au taux applicable dans la commune où est situé votre établissement '
(recherche par code postal et par code Commune) :
###=>>>> Dévloppé par DAH
-Taxe d'apprentissage  => Employeur sur Totalité du salaire'
La taxe d'apprentissage est basée sur la masse salariale de l'année précédente. Il s'agit de la somme des montants suivants :'
'Rémunérations soumises aux cotisations sociales (y compris les rémunérations versées aux salariés expatriés)'
Avantages en nature versés par l'entreprise (salaires, indemnités, primes, gratifications, cotisations salariales, pourboires notamment).'
Pour le calcul de la taxe, les rémunérations imposables sont arrondies à l'euro le plus proche (la fraction d'euro égale à 0,50 est comptée pour 1).

Le salaire des apprentis est exonéré totalement lorsque l'employeur a jusqu'à 10 salariés.
A=((T1)+(T2))
B=((T1)+(T2))  
result = ((A)-(B)%1)*0.0068
result = round(A)*0.0068
else:  
    result=0

(7) En alsace-Moselle : 0.44

result = ((T1)+(T2))*0.0044
result = round(result)
else:  
    result=0
###=>>>> Dévloppé par DAH
- Participation formation - Cotisation de formation  ###=>>>> Dévloppé par DAH=> Employeur sur Totalité du salaire
Formation (au moins 11 salariés)(8)
(8) Taux spécial de 1,30 % pour les entreprises de travail temporaire d'au moins 11 salariés. '
Contributions spécifiques de 1 % sur la rémunération des salariés sous contrat à durée déterminée 
et de 2,10 % sur la rémunération des intermittents du spectacle quel que soit l'effectif.'

A=((T1)+(T2))
if Total nombre id employee= ETP >= 11   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (A)*  0.01
else:  
    result=0

Taux spécial de 1,30 % pour les entreprises de travail temporaire d'au moins 11 salariés. '

A=((T1)+(T2))

if Total nombre id employee= ETP >= 11   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (A)*0.013
else:  
    result=0

et de 2,10 % sur la rémunération des intermittents du spectacle quel que soit l'effectif.'

A=((T1)+(T2))

result = (A)*0.021

Les entreprises du BTP sont redevables d'une cotisation spécifique dont le taux est fixé, quel que soit l'effectif, à 0,30 % pour les entreprises relevant du seul secteur du bâtiment 

A=((T1)+(T2))

result = (A)*0.003

et à 0,22 % dans celles relevant des travaux publics. Dans les entreprises d'au moins 11 salariés, cette cotisation est déductible de la contribution de droit commun de 1 %.'

A=((T1)+(T2))

if Total nombre id employee= ETP >= 11   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (A)*  0.0022
else:  
    result=0

###=>>>> Dévloppé par DAH
- Participation formation - Cotisation de formation => Employeur sur Totalité du salaire
Formation  (moins de 11 salariés)

A=((T1)+(T2))
if Total nombre id employee= ETP < 11   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (A)*0.0055
else:  
    result=0

et de 2,10 % sur la rémunération des intermittents du spectacle quel que soit l'effectif.'
A=((T1)+(T2))
result = (A)*0.021

Les entreprises du BTP sont redevables d'une cotisation spécifique dont le taux est fixé, quel que soit l'effectif, à 0,30 % pour les entreprises relevant du seul secteur du bâtiment 

A=((T1)+(T2))

result = (A)*0.003

###=>>>> Dévloppé par DAH
Construction (au moins 50 salariés) =participation construction

La participation des employeurs à l'effort de construction (PEEC), appelé également dispositif du 1 % logement, '
est un investissement directement versé par les employeurs en faveur du logement des salariés. 
Cette obligation s'applique quelle que soit l'activité exercée ou la forme juridique de l'entreprise. '
La PEEC figure sur le bulletin de paie des salariés.

Elle possède 50 salariés ou plus
Le nombre de salariés reste supérieur ou égal à 50 pendant 5 années consécutives

Exemple :

Une entreprise emploie en 2021 plus de 50 salariés. Si l'effectif reste supérieur ou égal à 50 pendant 5 années consécutives (jusqu'à 2025), 
alors elle devra payer la PEEC à partir de 2026.

Le calcul de l'effectif au 31 décembre de l'année N se fait en fonction du temps de travail.

Temps complet(actif)    
Chaque salarié est pris en compte pour 1 unité.             
Temps partiel
Chaque salarié est pris en compte proportionnellement au temps de travail fixé dans le contrat de travail.
Travail à domicile/intermittent
Chaque salarié est pris en compte pour 1 unité.

Calcul de la PEEC
L'employeur soumis à la PEEC doit consacrer au minimum une quote-part de 0,45 % des rémunérations versées l'année N-1 
sous la forme d'investissements en faveur de la construction de logements à effectuer avant le 31 décembre de l'année N.

A=((T1)+(T2))
if Total nombre id employee= ETP >= 50   categorie_id A créer un champ et se base sur total des employés Actif ainsi pour les non activés il faut que la date de sortie soit de l'année encours'

    result = (A)*0,0045 
else:  
    result=0


BRUT SANS RS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<
Dans un dernier temps, il faut bien sûr identifier les cotisations sociales dont l'assiette va être modifiée suite à ce déclenchement de réintégration sociale :'
les cotisations de Sécurité sociale suivantes : maladie, vieillesse, allocations familiales, accidents du travail ;
les cotisations sociales avec la même assiette : FNAL, versement de transport, contribution solidarité autonomie, assurance chômage, 
taxe d’apprentissage, participation formation, participation construction, contribution au dialogue social, cotisations pénibilité ; 

Il faut tenir compte des règles de plafonnement applicables aux assiettes des cotisations, ce qui peut limiter le montant réintégré, voire le rendre nul. 
les cotisations de retraite complémentaire Arrco et Agirc. 

Le montant de la réintégration sociale qui apparaît en haut et en bas du bulletin comme un avantage en nature est de 1 064€. 

Les excédents de cotisations non déductibles sont soumis à cotisations de Sécurité sociale, d'assurance chômage et de retraite complémentaire'
Ils ne sont jamais soumis à cotisations de prévoyance complémentaire ni à CSG CRDS pour ne pas augmenter à nouveau l'assiette de la réintégration sociale'

La réintégration sociale permet de soumettre les montants non déductibles à cotisations salariales et patronales pour les seules cotisations qui n'ont pas encore été impactées.


BRUT SANS RS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<

SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS
cumul_T1 sans RS  => result =T1 sans RS +payslip.cumul_T1 sans RS
cumul_T2 sans RS  => result =T2 sans RS +payslip.cumul_T2 sans RS

T1 sans RS
if SC<SP:
    result= cumul salaire – base cotisations tranche 1 précédentes cumulées. => cumul_BRUT - payslip.cumul_T1 sans RS
else:  
    result = cumul PMSS – base cotisations tranche 1 précédentes cumulées.   => cumul_PMSS - payslip.cumul_T1 sans RS

T2 sans RS
if SC>SP:
    result = cumul des salaires – cumul PMSS – bases cotisations tranche 2 précédentes. => cumul_BRUT- cumul_PMSS - payslip.cumul_T2 sans RS
else: 
    result =  – base cotisations tranche 2 précédentes cumulées.                        =>   - payslip.cumul_T2 sans RS      #Vérifié   


4 PMSS cumulés = 4 * SP

cumul_4 P1 sans RS => result =4 P1 sans RS+payslip.4 P1 sans RS 

4 P1 sans RS

if SC  < 4*SP:
    result= cumul salaire – base cotisations 4 P1 précédentes cumulées. => cumul_BRUT- payslip.4 P1 sans RS
else:  
    result = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées. => 4 * SP - payslip.4 P1 sans RS


8 PMSS cumulés = 8 * SP

cumul_8 P1 sans RS => result =8 P1 sans RS +payslip.8 P1 sans RS

8 P1 sans RS

if SC < 8*SP:
    result= cumul salaire – base cotisations 8 P1 précédentes cumulées. => cumul_BRUT - payslip.8 P1 sans RS
else:  
    result = 8 cumul PMSS – base cotisations 8 P1 précédentes cumulées. => 8 * SP - payslip.8 P1 sans RS


###=>>>> Dévloppé par DAH
Les cotisations de retraite supplémentaire, prévoyance et mutuelle
Pour ce qui est des cotisations de prévoyance, elles suivent le système des tranches de la Sécurité sociale, 
donc la rémunération brute du salarié. Les taux appliqués dépendent généralement de la convention collective de l'employeur, '
et font donc partie des informations à demander en cas de mise en place du dossier de l'entreprise dans le logiciel de paie, '
ou bien en début d'année pour contrôler la mise à jour des taux.'

- Complémentaire incapacité, invalidité, décès Tr A  ###=>Employeur sur Salaire limité à 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

if 'prévoyance'==active
result =(T1 sans RS)*0.Tx COP

- Complémentaire incapacité, invalidité, décès Tr A ###=>Salarié sur sur Salaire entre 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

if 'prévoyance'==active
result =(T1 sans RS)*0.Tx COS

- Complémentaire incapacité, invalidité, décès Tr 2 ###=> Employeur sur Salaire limité à 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €.

if 'prévoyance'==active
    result = ( 8 P1 sans RS - T1 )*0.Tx COP      #result=(T2)*0.Tx COP  faut figer cette regle 


- Complémentaire incapacité, invalidité, décès Tr 2 ###=>Salarié sur sur Salaire entre 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €.

if 'prévoyance'==active
    result = ( 8 P1 sans RS  - T1 )*0.Tx COS           #result =(T2)*0.Tx COS faut figer cette regle 

###=>>>> Dévloppé par DAH
Contrairement à la prévoyance, la mutuelle est généralement assise sur le PMSS et c'est donc une cotisations plafonnée. '
Au niveau des taux, ils sont fixés par le contrat passé entre l'entreprise et l'organisme de mutuelle. 
Il faut donc, comme pour la prévoyance, s'assurer de les demander à l'employeur.

La répartition des taux employeur/salarié pour ces cotisations doit au minimum être de 50/50.  COS = COP 

- Complémentaire santé (mutuelle) Tr 1  ###=>Employeur sur Salaire limité à 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

if 'mutuelle'==active
result =(T1 sans RS)*0.Tx COP

- Complémentaire santé (mutuelle) Tr 1  ###=>Salarié sur sur Salaire entre 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

if 'mutuelle'==active
result =(T1 sans RS)*0.Tx COS

###=>>>> Dévloppé par DAH
""""""""""""""""""""""""""""""""""""""""""
Le forfait social  # uniquement sur la partie exclue des cotisations de Sécurité sociale  
(si COP < Limite exo =>     soumis à CSG/CRDS + forfait social
    sinon 0)         => Not soumis à CSG/CRDS + forfait social
# Rappel : les montants patronaux exonérés de cotisations sont en revanche soumis à CSG (contribution sociale généralisée), 
# CRDS (contribution au remboursement de la dette sociale) et à forfait social.

Le forfait social est prélevé sur les rémunérations ou gains exonérés de cotisations de Sécurité sociale,  
mais est tout de même assujetti à la contribution sociale généralisée (CSG).

Il est important ici de détailler les éléments de rémunération qui sont soumis au forfait social :
les sommes versées au titre de l'intéressement ou de la participation ;'

les abondements de l'employeur aux plans d'épargne d'entreprise (PEE), aux plans d'épargne interentreprises (PEI) 
ou aux plans d'épargne pour la retraite collectifs (Perco) ;'

les contributions patronales de retraite supplémentaire et de prévoyance complémentaire 
(uniquement sur la partie exclue des cotisations de Sécurité sociale) ;

la prise en charge par l'employeur de la cotisation salariale au régime de retraite complémentaire ;'

les indemnités de rupture conventionnelle ;

les rémunérations perçues par les dirigeants, administrateurs et membres des conseils de surveillance des sociétés anonymes (SA)
 et des sociétés d'exercice libéral (SEL) à forme anonyme, pour l'exercice de leur mandat, sous forme de jetons de présence ;

les rémunérations exceptionnelles allouées par le conseil d'administration ou par le conseil de surveillance pour les missions '
et mandats confiés à des administrateurs.

Le forfait social  = result = k + l + PEE + PEI + Perco + COS_Ret_supp_prisencharge + IRC + jetons_présence + jetons_présence_except

controle = payslip.prévoyance
controle = payslip.mutuelle
controle = payslip.retraite supplémentaire
a = active = obligatoire and collectif
if 'prévoyance'==a and if 'mutuelle'==a and if 'retraite supplémentaire'==a

controle = payslip.prévoyance
if controle:

- Complémentaire incapacité, invalidité, décès Tr A  ###=>Employeur sur Salaire limité à 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

if 'prévoyance'==active
result =(T1 sans RS)*0.Tx COP

- Complémentaire incapacité, invalidité, décès Tr 2 ###=> Employeur sur Salaire limité à 1 P et 8 P >>>2020: PMSS tranche 2 : de 3 428 € à 27 424 €.

if 'prévoyance'==active
    result = ( 8 P1 sans RS - T1 )*0.Tx COP      #result=(T2)*0.Tx COP  faut figer cette regle 

- Complémentaire santé (mutuelle) Tr 1  ###=>Employeur sur Salaire limité à 1 P  >2020: PMSS tranche 1(1 P) : de 0 € à 3 428 €

controle = payslip.mutuelle
if controle:

if 'mutuelle'==active
result =(T1 sans RS)*0.Tx COP

result= COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1
result = Complémentaire incapacité, invalidité, décès Tr A  + Complémentaire incapacité, invalidité, décès Tr 2 (1 P et 8 P) + Complémentaire santé (mutuelle) Tr 1 

cumul_COP Prevoyance T1 =  COP Prevoyance T1 + payslip.cumul_COP Prevoyance T1
cumul_COP Prevoyance T2 =  COP Prevoyance T2 + payslip.cumul_COP Prevoyance T2
cumul_COP mutuelle T1   =  COP mutuelle T1 + payslip.cumul_COP mutuelle T1
SP = cumul_PMSS => result =PMSS+payslip.PMSS 


controle = payslip.prévoyance + payslip.mutuelle
a = cumul_COP Prevoyance T1
b = cumul_COP Prevoyance T2
a1 = cumul_COP mutuelle T1
c = O.O6 * SP
d = 0.015  * cumul_BRUT
e = 0.12 * SP
###=>>>> Dévloppé par DAH
g = Limite d'exonération'
###=>>>> Dévloppé par DAH
if (c+d) < e
    result = c + d
else : 
    result = e

g_mens = g - payslip.cumul_g

cumul_k = k + payslip.cumul_k

k  = # uniquement sur la partie exclue des cotisations de Sécurité sociale     
if controle:

    if (a+b+a1)>g:  
        #result= g_mens 
        result= g -  payslip.cumul_k
    else:
        #result=COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1
        result = (a+b+a1) -  payslip.cumul_k     

cumul_COP retraite_supplémentaire  =  COP retraite_supplémentaire + payslip.cumul_COP retraite_supplémentaire

controle = payslip.retraite_supplémentaire
a = cumul_COP retraite_supplémentaire  => ses cotisations de retraite supplémentaire, entièrement prises en charge par l'employeur, s'élèvent à            € annuels.
c = 0.05 * SP           # =>   41 136 * 5% = 2 056€
d = 0.05  * cumul_BRUT  # => Un salarié touche = 250 000€ * 5% or soit au maximum 205 680 x 5% = 10 284 euros pour 2020
e = 0.05 * 5 * SP        #=>  41 136 * 5 * 5% = 10 284€

###=>>>> Dévloppé par DAH
g = Limite d'exonération'  #=>  Limite_exonération dans le cas où la rémunération prise en compte est au maximum égale à 5 PASS applicables au salarié (soit au maximum 205 680 x 5% = 10 284 euros pour 2020).
Étape 1 : => comparer aux 5% de la rémunération annuelle limitée à 5 plafonds et la rémunération annuelle
###=>>>> Dévloppé par DAH
if d < e
    result = d
else : 
    result = e

###=>>>> Dévloppé par DAH Les parts patronales des régimes de retraite supplémentaire sont exonérées de cotisations si leur montant ne dépasse pas l’une des deux limites suivantes (la plus élevée des deux) :
h = la plus élevée des deux  => comparer aux 5% du plafond annuel de Sécurité sociale et 5% de la rémunération annuelle limitée à 5 plafonds
###=>>>> Dévloppé par DAH
if c < g
    result = g
else : 
    result = c

h_mens = h - payslip.cumul_h

cumul_l = l + payslip.cumul_l

l = # uniquement sur la partie exclue des cotisations de Sécurité sociale  
if controle:

    if a>h:  
        #result= h_mens 
        result= h -  payslip.cumul_l

    else:
        #result=COP retraite_supplémentaire
        result = a -  payslip.cumul_l


alors l'assiette le forfait social' =

result = k + l + PEE + PEI + Perco + COS_Ret_supp_prisencharge + IRC + jetons_présence + jetons_présence_except

Le taux du forfait social est fixé à 20 %, mais parfois des taux de 8 et 16 % peuvent s'appliquer.'

Forfait social

Le forfait social au taux de 20 % est déclaré avec le code type de personnel : 012.

Pour les régimes de retraite supplémentaire non éligibles à l’exonération ou pour les parties des contributions dépassant les limites d’exonération, le forfait social n’est pas dû.

Le forfait social à 16 % ne concerne que certains versements alimentant un plan d’épargne pour la retraite collectif (Perco).
# Sous conditions, un taux réduit de forfait social peut s’appliquer.
# Il faut pour cela que le règlement du plan d'épargne respecte deux conditions, précisées à l'article L 137-16 al. 7 du Code de la Sécurité sociale :
# 1° Les sommes recueillies sont affectées par défaut, dans les conditions prévues au second alinéa de l'article L. 3334-11 du même code.
# 2° L'allocation de l'épargne est affectée à l'acquisition de parts de fonds, dans des conditions fixées par décret, qui comportent au moins 7 % de titres susceptibles d'être employés dans un plan d'épargne en actions destiné au financement des petites et moyennes entreprises et des entreprises de taille intermédiaire, dans les conditions prévues à l'article L. 221-32-2 du Code monétaire et financier."
# Si ces deux conditions sont respectées, alors le taux du forfait social à appliquer sera de 16 %.
result = Perco * 0.16

Les contributions patronales au financement de prestations de retraite supplémentaire exonérées de cotisations de Sécurité sociale 
sont soumises à la contribution dite « forfait social ».

Le taux du forfait social est de 8 % pour :

les contributions des employeurs destinées au financement des prestations complémentaires de prévoyance versées au bénéfice de leurs salariés,
anciens salariés et de leurs ayants droit ;

la réserve spéciale de participation dans les sociétés coopératives et participatives.

result = RSP_Scop * 0.08

Les entreprises franchissant le seuil des 11 salariés au titre de 2016, 2017 ou 2018 
bénéficient d'une exonération du forfait social de 8 % sur les cotisations patronales de prévoyance et de mutuelle pendant 3 ans'
###=>>>> Dévloppé par DAH
Base Forfait Social 8% 
Contributions patronales de retraite supplémentaire et de prévoyance complémentaire (sur la partie exonérée de cotisations de sécurité sociale)

result = (k + l) * 0.08

                             <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
La réintégration sociale et fiscale :

Le principe de réintégration sociale et fiscale en France désigne une règle selon laquelle 
les montants des cotisations patronales de prévoyance et de retraite supplémentaire sont exonérés de cotisations sociales dans une certaine limite, imposée chaque année par la loi

Cela implique donc que si ces montants dépassent la limite imposée, alors l'excédent sera réintégré à l'assiette des cotisations sociales,  =>  Brut Avec RS
c'est ce qu'on appelle la réintégration sociale ; ou au salaire net imposable, c'est la réintégration fiscale.'

La réintégration sociale

Concernant la retraite supplémentaire :
les parts patronales des cotisations de retraites supplémentaires dites « art 83 » ;
les parts du Comité social et économique (CSE) finançant ces régimes de retraites supplémentaires ;
le montant des abondements exonérés de l’employeur au Plan d’épargne pour la retraite collectif (Perco)

Concernant la Prévoyance et mutuelles:
les parts patronales des cotisations de prévoyance complémentaire et mutuelle ;
les parts du CSE finançant ces régimes de prévoyance et mutuelle

Il faut que le régime de retraite ou de prévoyance concerné ait un caractère à la fois obligatoire et collectif. 
Cela signifie que tous les salariés faisant partie de l'entreprise, sans exception, doivent souscrire à ce régime.'
Sont exclues toutes contributions à des régimes non obligatoires, qui n’ont pas de caractère collectif. Et qui restent par conséquent entièrement soumises à cotisations.

Rappel : les montants patronaux exonérés de cotisations sont en revanche soumis à CSG (contribution sociale généralisée), 
CRDS (contribution au remboursement de la dette sociale) et à forfait social.

Tout d'abord, il n'y a que la partie qui est supérieure à la limite d'exonération'
qui doit être ajoutée à l'assiette des cotisations sociales.'
Ensuite, le plafond annuel de la Sécurité sociale à prendre en compte doit correspondre au plafond annuel du salarié, 
donc en tenant compte, le cas échéant, d'absences non rémunérées, de temps partiel ou de tout autre prorata 'qui aurait eu lieu pour chacun des salariés concernés.

Dans un dernier temps, il faut bien sûr identifier les cotisations sociales dont l'assiette va être modifiée suite à ce déclenchement de réintégration sociale :'

les cotisations de Sécurité sociale suivantes : maladie, vieillesse, allocations familiales, accidents du travail ;

les cotisations sociales avec la même assiette : FNAL, versement de transport, contribution solidarité autonomie, assurance chômage, 
taxe d’apprentissage, participation formation, participation construction, contribution au dialogue social, cotisations pénibilité ;

Il faut tenir compte des règles de plafonnement applicables aux assiettes des cotisations, ce qui peut limiter le montant réintégré, voire le rendre nul.
les cotisations de retraite complémentaire Arrco et Agirc.

###=>>>> Dévloppé par DAH

controle = payslip.prévoyance
controle = payslip.mutuelle
controle = payslip.retraite supplémentaire
a = active = obligatoire and collectif
if 'prévoyance'==a and if 'mutuelle'==a and if 'retraite supplémentaire'==a

Pour ce qui est des cotisations patronales de prévoyance dans un premier temps, elles sont exonérées dans la limite de la somme de ces deux + montants:

6 % du PASS applicable au salarié (soit 2 468,16 euros en 2020 pour un salarié à temps plein, présent toute l’année) ;
+ y ajouter
1,5 % de la rémunération brute annuelle du salarié.

Sachant que la somme de ces deux montants ne peut toutefois pas dépasser une limite supplémentaire : 12 % du montant du PASS applicable au salarié (soit 4 936,32 euros en
2020 pour un salarié à temps plein présent toute l’année).
vérifier que ce total est bien inférieur à 12% du plafond de la Sécurité sociale.
Le total des contributions exonérées ne peut pas excéder 12 % du montant du plafond de la Sécurité sociale.

###=>>>> Dévloppé par DAH
PASS: 41 136,00   pour un salarié à temps plein  2020
Multiple    Montant du plafond correspondant      
6 %                2468,16 €     
+ 
1,5 %  * cumul_BRUT  de la rémunération brute annuelle du salarié.       

ne pas dépasser une limite 12 % du montant du PASS applicable au salarié   soit 4 936,32 € 

Le plafond d'exonération des cotisations patronales à un régime de prévoyance complémentaire concerne à la fois la prévoyance complémentaire et les régimes de prévoyance'
dits « frais de santé » qui respectent les conditions d'exonération et répondent au cahier des charges des contrats responsables.'

En cas de dépassement du plafond d'exonération, la réintégration dans l'assiette des cotisations devient obligatoire.

Les excédents de cotisations non déductibles sont soumis à cotisations de Sécurité sociale, d'assurance chômage et de retraite complémentaire. '
Ils ne sont jamais soumis à cotisations de prévoyance complémentaire ni à CSG CRDS pour ne pas augmenter à nouveau l'assiette de la réintégration sociale.' 

(si COP < Limite exo =>     soumis à CSG/CRDS 
    sinon 0)         => Not soumis à CSG/CRDS

La réintégration sociale permet de soumettre les montants non déductibles à cotisations salariales et patronales 
pour les seules cotisations qui n'ont pas encore été impactées.' ????????

Elle permet aussi, sauf lorsque les montants proviennent d'une mutuelle, déjà soumise à réintégration fiscale, d'augmenter le net imposable du salarié.

Exemple de calcul de l'exonération des cotisations patronales de prévoyance et mutuelle avec réintégration sociale'  avec RS

Un salarié touche une rémunération brute annuelle de 30 000€. Le cumul des cotisations patronales de prévoyance et mutuelle s'élève à 4 000€ (cas d'école).

Étape 1 : calculer 6% du PASS

On obtient 3 428 * 12 * 6% = 2 468,16€

Étape 2 : ajouter 1,50% de la rémunération

30 000 * 1,50% = 450€

Soit un maximum exonéré de 2 468€ + 450€ = 2 936€ (arrondi)

Étape 3 : comparer ce montant à la somme de 12 % du PASS

Le PASS vaut 41 136€.

41 136 * 12% = 4 936€ arrondi

L'exonération est limitée pour ce salarié, à 2 936 €.'

result= COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1
result = Complémentaire incapacité, invalidité, décès Tr A  + Complémentaire incapacité, invalidité, décès Tr 2 (1 P et 8 P) + Complémentaire santé (mutuelle) Tr 1 

cumul_COP Prevoyance T1 =  COP Prevoyance T1 + payslip.cumul_COP Prevoyance T1
cumul_COP Prevoyance T2 =  COP Prevoyance T2 + payslip.cumul_COP Prevoyance T2
cumul_COP mutuelle T1   =  COP mutuelle T1 + payslip.cumul_COP mutuelle T1

SP = cumul_PMSS => result =PMSS+payslip.PMSS  ###=> sera calculé en fonction *
# * le PASS applicable doit correspondre au plafond annuel du salarié, c’est-à-dire qu’il doit tenir compte, si c’est le cas, 
#  d’absences non rémunérées, de temps partiel ou de tout autre prorata qui aurait eu lieu dans l’année.

controle = payslip.prévoyance + payslip.mutuelle
a = cumul_COP Prevoyance T1
b = cumul_COP Prevoyance T2
a1 = cumul_COP mutuelle T1
c = 0.06 * SP           => Étape 1 : calculer 6% du PASS  On obtient   3 428 * 12 * 6% = 2 468,16€
d = 0.015  * cumul_BRUT => Étape 2 : ajouter 1,50% de la rémunération  30 000 * 1,50% = 450€ Soit un maximum exonéré de 2 468€ + 450€ = 2 936€ (arrondi)
e = 0.12 * SP           => Étape 3 : calculer la somme de 12% du PASS Le PASS vaut 41 136€. 41 136 * 12% = 4 936€ arrondi


###=>>>> Dévloppé par DAH 
g = Limite d'exonération'      #=>  Limite_exonération Étape 3 : comparer ce montant à la somme de 12% du PASS Le PASS vaut 41 136€. 41 136 * 12% = 4 936€ arrondi
###=>>>> Dévloppé par DAH      vérifier que ce total est bien inférieur à 12% du plafond de la Sécurité sociale.
if (c+d) < e                   # ne pas dépasser une limite 12 % du montant du PASS applicable au salarié   soit 4 936,32  pour un salarié à temps plein  2020
    result = c + d
else : 
    result = e

g_mens = g - payslip.cumul_g

cumul_RS1 ###=>>>> Dévloppé par DAH => Excédent_socialePr_reintegre

if controle:

    if (a+b+a1)>g:  
        result= ((a+b+a1)-g) # alors l'excédent sera réintégré à l'assiette des cotisations sociales  => Excédent_socialePr_reintegre = 1064
    else:
        result=0

RS1 = cumul_RS1 - payslip.cumul_RS1 

Un salarié touche une rémunération brute annuelle de 30 000€. Le cumul des cotisations patronales de prévoyance et mutuelle s'élève à 4 000€ (cas d'école).

La part patronale de la prévoyance complémentaire dépasse ce montant,  4000 > 2 936
il faudra soumettre le surplus à cotisations sociales.  (4000 - 2936) = 1064
Le montant de la réintégration sociale qui apparaît en haut et en bas du bulletin comme un avantage en nature est de 1 064€.

Pour éviter la réintégration unique en fin d'année, qui peut impacter lourdement le salaire net à payer du salarié, '
il est possible de paramétrer le logiciel de paie pour obtenir une réintégration sociale mensuelle. 
Dans le cas présent, ce sont 88,67€ par mois qu'il faudra réintégrer socialement.'

                    RS1 = cumul_RS1 - payslip.cumul_RS1 

Concernant la retraite supplémentaire : L’entreprise peut proposer à son effectif un système de retraite supplémentaire sous forme de contrat retraite « article 83 » 
Ces contributions sont soumises à la CSG et à la CRDS et au forfait social au taux de 20 %.
Transfert des droits CET vers un régime de retraite
les abondements Perco dans la limite de 16% du PASS ;
Abondement de l’employeur à un Perco / Le montant maximum de l’abondement au Perco exonéré de cotisations est fixé à 16 % du plafond annuel de la Sécurité sociale.

Exemple :
Un salarié perçoit une rémunération annuelle égale au plafond de la Sécurité sociale (41 136 € en 2022).
La limite d’exonération des contributions patronales est de 2 057 € (5 % du plafond annuel). Si le montant de l’abondement au Perco s’élève à 650 €, 
la limite d’exclusion applicable aux contributions patronales de retraite sera égale à 1 407 € (2 057 € - 650 €).

Limite d’exclusion -= Limite - PERCO - CET_PERCO

Pour ce qui est des cotisations patronales de retraite supplémentaire dans un second temps, elles sont exonérées dans la limite de :

5 % du plafond de la Sécurité sociale ;

ou bien 5 % de la rémunération retenue jusqu’à 5 plafonds de Sécurité sociale.

Les parts patronales des régimes de retraite supplémentaire sont exonérées de cotisations si leur montant ne dépasse pas l’une des deux limites suivantes (la plus élevée des deux) :

5 % du plafond annuel de sécurité sociale (PASS) applicable au salarié* (ce qui correspond à 2 056,80 euros pour l’année 2020 pour un salarié à temps plein, présent toute l’année) ;
ou 5 % de la rémunération brute annuelle, dans le cas où la rémunération prise en compte est au maximum égale à 5 PASS applicables au salarié 
(soit 5% de la rémunération annuelle brute soumise à cotisations jusqu'à 5 PASS maximum' (soit au maximum 205 680 x 5% = 10 284 euros pour 2020).)

controle = retraite supplémentaire
a = active = obligatoire et collectif
if 'retraite supplémentaire'==a

cumul_COP retraite_supplémentaire  =  COP retraite_supplémentaire + payslip.cumul_COP retraite_supplémentaire

SP = cumul_PMSS => result =PMSS+payslip.PMSS  ###=> sera calculé en fonction *
# * le PASS applicable doit correspondre au plafond annuel du salarié, c’est-à-dire qu’il doit tenir compte, si c’est le cas, 
#  d’absences non rémunérées, de temps partiel ou de tout autre prorata qui aurait eu lieu dans l’année.

Exemple de calcul de l'exonération d'une retraite supplémentaire avec réintégration sociale

Un salarié touche 250 000€ par an et ses cotisations de retraite supplémentaire, entièrement prises en charge par l'employeur, s'élèvent à 12 500€ annuels.

Étape 1 : calculer 5% de la rémunération annuelle limitée à 5 plafonds

41 136 * 5 * 5% = 10 284€

Étape 2 : comparer aux 5% du plafond annuel de Sécurité sociale

41 136 * 5% = 2 056€

La réintégration sociale s'élève à 12 500 - 10 284 = 2 216€ par an'


controle = payslip.retraite_supplémentaire
a = cumul_COP retraite_supplémentaire  => ses cotisations de retraite supplémentaire, entièrement prises en charge par l'employeur, s'élèvent à 12 500€ annuels.
c = 0.05 * SP           # =>   41 136 * 5% = 2 056€
d = 0.05  * cumul_BRUT  # => Un salarié touche = 250 000€ * 5% or soit au maximum 205 680 x 5% = 10 284 euros pour 2020
e = 0.05 * 5 * SP        #=>  41 136 * 5 * 5% = 10 284€

###=>>>> Dévloppé par DAH
g = Limite d'exonération'#=>Limite_exonération dans le cas où la rémunération prise en compte est au maximum égale à 5 PASS applicables au salarié (soit au maximum 205 680 x 5% = 10 284 euros pour 2020).
Étape 1 : => comparer aux 5% de la rémunération annuelle limitée à 5 plafonds et 5%  de la rémunération annuelle
###=>>>> Dévloppé par DAH
if d < e
    result = d
else : 
    result = e
###=>>>> Dévloppé par DAH => Excédent_socialePr_reintegre

###=>>>> Dévloppé par DAH Les parts patronales des régimes de retraite supplémentaire sont exonérées de cotisations si leur montant ne dépasse pas l’une des deux limites suivantes (la plus élevée des deux) :
h = la plus élevée des deux  => comparer aux 5% du plafond annuel de Sécurité sociale et 5% de la rémunération annuelle limitée à 5 plafonds
###=>>>> Dévloppé par DAH
if c < g
    result = g
else : 
    result = c


cumul_RS2###=>>>> Dévloppé par DAH => Excédent_socialeRet_reintegre 

if controle:

    if a>h:  
        result= a-h # alors l'excédent sera réintégré à l'assiette des cotisations sociales  => Excédent_socialeRet_reintegre
                    # La réintégration sociale s'élève à 12 500 - 10 284 = 2 216€ par an'
    else:
        result=0

RS2 = cumul_RS2 - payslip.cumul_RS2
                                                        

La réintégration fiscale
En effet, le principe est le suivant :

Les cotisations patronales aux régimes de retraite supplémentaire et de prévoyance complémentaire versées au bénéfice des salariés 
sont exonérées de cotisations de sécurité sociale (régime social).

Et les cotisations salariales ET patronales de retraite supplémentaire et de prévoyance complémentaire sont exonérées d’impôts (régime fiscal).

Le principe est le même que pour la réintégration sociale mais vous l'aurez compris,'
il s'agit ici de réintégrer dans le salaire net imposable les montants qui dépasseraient les limites imposées par la loi.'
En sachant que la part patronale des frais de santé est automatiquement réintégrée fiscalement.
"""""""""
Pour rappel, les cotisations patronales de frais de santé appelées également part patronale de mutuelle sont réintégrées fiscalement dès le 1er euro.
"""""""""
Ainsi, nous retrouvons notre part patronale de prévoyance, à caractère obligatoire et collectif d'une part,'
et notre part patronale de retraite supplémentaire, toujours à caractère obligatoire et collectif d'autre part. ;)'
En plus des cotisations patronales de ces deux régimes, il faut également, pour calculer la réintégration fiscale, + prendre en compte les cotisations salariales.

"""""""""
Concernant les cotisations patronales de prévoyance complémentaire : elles sont exonérées du prélèvement de l’impôt sur le revenu dans les limites suivantes :
"""""""""
5% du montant annuel PSS + 2% de la rémunération annuelle brute du salarié. Le total obtenu ne peut pas dépasser 2% de 8 fois le montant annuel PSS (art.83,1°quater du CGI).
Pour ce qui est des limites données par la loi :

Les montants des cotisations patronales de prévoyance ne doivent pas dépasser :

5 % du plafond annuel de la Sécurité sociale (2 056,80 € en 2020) majorés de 2 % de la rémunération annuelle brute ;

Le total des cotisations exonérées ne peut pas dépasser 2 % de 8 fois le montant annuel du plafond de la Sécurité sociale (soit 6 581,76 € en 2020).

###=>>>> Dévloppé par DAH

controle = payslip.prévoyance
#controle = payslip.mutuelle
a = active = obligatoire and collectif
if 'prévoyance'==a #and if 'mutuelle'==a 

RF1 = cumul_RF1 - payslip.cumul_RF1 

result= COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)#+ COP mutuelle T1
result = Complémentaire incapacité, invalidité, décès Tr A  + Complémentaire incapacité, invalidité, décès Tr 2 (1 P et 8 P) #+ Complémentaire santé (mutuelle) Tr 1 

cumul_COP Prevoyance T1 =  COP Prevoyance T1 + payslip.cumul_COP Prevoyance T1
cumul_COP Prevoyance T2 =  COP Prevoyance T2 + payslip.cumul_COP Prevoyance T2

#cumul_COP mutuelle T1   =  COP mutuelle T1 + payslip.cumul_COP mutuelle T1

SP = cumul_PMSS => result =PMSS+payslip.PMSS  ###=> sera calculé en fonction *
# * le PASS applicable doit correspondre au plafond annuel du salarié, c’est-à-dire qu’il doit tenir compte, si c’est le cas, 
#  d’absences non rémunérées, de temps partiel ou de tout autre prorata qui aurait eu lieu dans l’année.

controle = payslip.prévoyance + payslip.mutuelle
a = cumul_COP Prevoyance T1
b = cumul_COP Prevoyance T2
#a1 = cumul_COP mutuelle T1
c = 0.05 * SP           # =>   Étape 1 : calculer 5% du PASS  On obtient   3 428 * 12 * 5% = 2 056€ => 41 136 * 5% = 2 056€  
d = 0.02  * cumul_BRUT  # =>   Étape 2 : ajouter 2% de la rémunération annuelle brute 
e = 0.02 * 8 * SP        #=>   Étape 3 : calculer la somme de 2% du 8 fois PASS Le PASS vaut 41 136€. 41 136 * 8 * 2% = 6 581,76 € . =>  329 088 * 2% = 6 581,76 €

###=>>>> Dévloppé par DAH
g = Limite d'exonération'  #=>  Limite_exonération dans le cas où la rémunération prise en compte est au maximum égale au
                           # total des cotisations exonérées ne peut pas dépasser 2 % de 8 fois le montant annuel du plafond de la Sécurité sociale (soit 6 581,76 € en 2020).
                           # Étape 3 : => comparer aux 2 % de 8 fois PASS (soit 6 581,76 € en 2020).
if (c+d) < e                   
    result = c + d
else : 
    result = e

cumul_RF1 ###=>>>> Dévloppé par DAH => Excédent_fiscal_Pr_reintegre

if controle:

    if (a+b)>g:  
        result= ((a+b)-g) # alors l'excédent sera réintégré à l'assiette fiscale  => Excédent_fiscal_Pr_reintegre
    else:
        result=0

Les montants des cotisations patronales de retraite supplémentaire ne doivent pas, quant à eux, dépasser :

8 % de la rémunération annuelle brute limitée à 8 % de 8 fois le montant annuel du plafond de la Sécurité sociale, soit une limite maximale absolue de 26 327 € en 2020.

Pour le cas de la retraite supplémentaire, la limite doit être diminuée dans les cas suivants :

abondement de l’employeur à un plan d’épargne pour la retraite collectif (PERCO) ;

sommes issues d’un compte épargne-temps (CET) et correspondant à un abondement de l’employeur utilisées pour financer un PERCO.

Exemple :
Un salarié perçoit une rémunération annuelle égale au plafond de la Sécurité sociale (41 136 € en 2022).
La limite d’exonération des contributions patronales est de 2 057 € (5 % du plafond annuel). Si le montant de l’abondement au Perco s’élève à 650 €, 
la limite d’exclusion applicable aux contributions patronales de retraite sera égale à 1 407 € (2 057 € - 650 €).

Limite -= Limite - PERCO - CET_PERCO
 
controle = payslip.retraite supplémentaire
a = active = obligatoire and collectif
if 'retraite supplémentaire'==a

cumul_COP retraite_supplémentaire  =  COP retraite_supplémentaire + payslip.cumul_COP retraite_supplémentaire

SP = cumul_PMSS => result =PMSS+payslip.PMSS  ###=> sera calculé en fonction *
# * le PASS applicable doit correspondre au plafond annuel du salarié, c’est-à-dire qu’il doit tenir compte, si c’est le cas, 
#  d’absences non rémunérées, de temps partiel ou de tout autre prorata qui aurait eu lieu dans l’année.

controle = payslip.retraite_supplémentaire
a = cumul_COP retraite_supplémentaire #=> ses cotisations de retraite supplémentaire, entièrement prises en charge par l'employeur'
d = 0.08  * cumul_BRUT                 #=>   Étape 1 : calculer 8% de la rémunération annuelle brute 
e = 0.08 * 8 * SP                      #=>   Étape 2 : calculer la somme de 8% du 8 fois PASS Le PASS vaut 41 136€. 41 136 * 8 * 8% = 26 327 €      329 088 * 8% 

###=>>>> Dévloppé par DAH
g = Limite d'exonération'  #=>  Limite_exonération dans le cas où la rémunération prise en compte est au maximum égale au
                           # total des cotisations exonérées ne peut pas dépasser 8 % de 8 fois le montant annuel du plafond de la Sécurité sociale (soit 26 327 € en 2020).
                           # Étape 3 : => comparer 8% de la rémunération annuelle brute aux 8 % de 8 fois PASS (soit 26 327 €  en 2020).

###=>>>> Dévloppé par DAH
g = Limite d'exonération'  #=>  Limite_exonération dans le cas où la rémunération prise en compte est au maximum égale à 8 PASS applicables au salarié (soit au maximum 41 136 * 8 * 8% = 26 327 €  pour 2020).
Étape 3 : => comparer aux 8% de la rémunération annuelle limitée à 8 plafonds (soit au maximum 41 136 * 8 * 8% = 26 327 €  pour 2020).
###=>>>> Dévloppé par DAH
if d < e
    result = d
else : 
    result = e
###=>>>> Dévloppé par DAH => Excédent_fiscl_Ret_sup_reintegre

cumul_RF2###=>>>> Dévloppé par DAH => Excédent_fiscl_Ret_sup_reintegre

if controle:

    if a>g:  
        result= a-g # alors l'excédent sera réintégré à l'assiette fisclae  => Excédent_fiscla_Ret_sup_reintegre
    else:
        result=0

RF2 = cumul_RF2 - payslip.cumul_RF2

###=>>>> Dévloppé par DAH ###=>Salarié sur assiette de la CSG et de la CRDS

Identifiez les cas particuliers : CSG/CRDS
Les cotisations à la charge du salarié :

La contribution sociale généralisée (CSG)
D'après l'Urssaf, la CSG et la CRDS sont calculées sur "tous les éléments soumis à cotisations de Sécurité sociale". 
En d'autres termes, cela signifie que comme pour les autres cotisations, le calcul se fait sur le salaire brut.'
Cette cotisation est prélevée sur les revenus bruts des salariés mais aussi sur les revenus de remplacement(allocations chômage ou d'indemnités pour cause de maladie)'
d'avantages en nature ou en espèces, de primes et indemnités diverses, de bénéfices industriels, commerciaux ou agricoles, par exemple.'

Il est important également de retenir que certains revenus sont exonérés de CSG (et de CRDS), comme par exemple les sommes perçues par les étudiants ou les apprentis, 
les sommes perçues dans le cadre du volontariat ou de la coopération, ou encore les frais professionnels.

La contribution au remboursement de la dette sociale (CRDS) Le fonctionnement est le même que pour la CSG en termes de revenus.

La CSG et la CRDS sont dues, quel que soit le régime social applicable aux contributions patronales de retraite supplémentaire.

Les contributions patronales de retraite supplémentaire sont assujetties en totalité à CSG-CRDS sans application de l’abattement pour frais professionnels.

###=>>>> Dévloppé par DAH
l'assiette du calcul de la CSG et de la CRDS' => Base CSG/CRDS = assiette de la CSG et de la CRDS:

# uniquement sur la partie exclue des cotisations de Sécurité sociale  
(si COP < Limite exo =>     soumis à CSG/CRDS + forfait social
    sinon 0)         => Not soumis à CSG/CRDS + forfait social
#Rappel : les montants patronaux exonérés de cotisations sont en revanche soumis à CSG (contribution sociale généralisée),CRDS (contribution au remboursement de la dette sociale) et à forfait social.

Les excédents de cotisations non déductibles sont soumis à cotisations de Sécurité sociale, d'assurance chômage et de retraite complémentaire. '
Ils ne sont jamais soumis à cotisations de prévoyance complémentaire ni à CSG/CRDS pour ne pas augmenter à nouveau l'assiette de la réintégration sociale.' 

(si COP < Limite exo =>     soumis à CSG/CRDS 
    sinon 0)         => Not soumis à CSG/CRDS

result= COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1
result = Complémentaire incapacité, invalidité, décès Tr A  + Complémentaire incapacité, invalidité, décès Tr 2 (1 P et 8 P) + Complémentaire santé (mutuelle) Tr 1 

cumul_COP Prevoyance T1 =  COP Prevoyance T1 + payslip.cumul_COP Prevoyance T1
cumul_COP Prevoyance T2 =  COP Prevoyance T2 + payslip.cumul_COP Prevoyance T2
cumul_COP mutuelle T1   =  COP mutuelle T1 + payslip.cumul_COP mutuelle T1
cumul_COP retraite_supplémentaire  =  COP retraite_supplémentaire + payslip.cumul_COP retraite_supplémentaire
SP = cumul_PMSS => result =PMSS+payslip.PMSS  ###=> sera calculé en fonction *

cumul_k = k + payslip.cumul_k

k  = # uniquement sur la partie exclue des cotisations de Sécurité sociale     
if controle:

    if (a+b+a1)>g:  
        #result= g_mens 
        result= g -  payslip.cumul_k
    else:
        #result=COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1
        result = (a+b+a1) -  payslip.cumul_k     

# g_mens = g - payslip.cumul_g

# k  = # uniquement sur la partie exclue des cotisations de Sécurité sociale     
# if controle:

#     if (a+b+a1)>g:  
#         result= g_mens 
#     else:
#         result=COP Prevoyance T1+ COP Prevoyance T2(1 P et 8 P)+ COP mutuelle T1

# h_mens = h - payslip.cumul_h

l = # uniquement sur la partie exclue des cotisations de Sécurité sociale  
if controle:

cumul_l = l + payslip.cumul_l

l = # uniquement sur la partie exclue des cotisations de Sécurité sociale  
if controle:

    if a>h:  
        #result= h_mens 
        result= h -  payslip.cumul_l



    else:
        #result=COP retraite_supplémentaire
        result = a -  payslip.cumul_l


    # if a>h:  
    #     result= h_mens 
    # else:
    #     result=COP retraite_supplémentaire


# k(cumul_COP Prevoyance T1 == a + cumul_COP Prevoyance T2 == b + cumul_COP mutuelle T1 == a1) + l() =>  uniquement sur la partie exclue des cotisations de Sécurité sociale  

Base CSG/CRDS :

    result= BRUT abattu + k + l

+Indemnités de mise à la retraite 
+Indemnités de licenciement ou de départ volontaire du plan social pour la partie qui excède les montants conventionnels ou légaux  
+les primes liées à la participation et à l’intéressement des salariés aux résultats de l’entreprise. 
+PEE + PEI + PERCO aux sommes versées au titre de l’épargne salariale (intéressement, participation, abondements aux plans d’épargne salariale)

#=> ce calcule doit être en cumulé et anualisé moins ce qui est payé avant progrissive

Le salaire brut peut bénéficier de ce qu'on appelle un abattement. Il s'agit tout simplement d'une déduction faite sur la rémunération brute du salarié.'
Cet abattement est de 1,75 %.

salaire brut * 1,75 % : cette méthode vous donne le montant de l'abattement, qu'il faudra par la suite retirer du salaire brut ;

salaire brut * 98,25 % : cette méthode vous donne directement le montant du salaire brut après abattement. 

=> Salaire brut * abattement = salaire brut abattu => BRUT abattu

Pour pouvoir bénéficier de cette déduction, il faut que le salaire brut ne dépasse pas le montant équivalant à quatre plafonds annuels de la Sécurité sociale.

BRUT SANS RS =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

SC = cumul_BRUT   => result =BRUT+payslip.BRUT 
SP = cumul_PMSS   => result =PMSS+payslip.PMSS
cumul_T1 sans RS  => result =T1 sans RS + payslip.cumul_T1 sans RS
cumul_T2 sans RS  => result =T2 sans RS + payslip.cumul_T2 sans RS

T1 sans RS
if SC<SP:
    result= cumul salaire – base cotisations tranche 1 précédentes cumulées. => cumul_BRUT - payslip.cumul_T1 sans RS
else:  
    result = cumul PMSS – base cotisations tranche 1 précédentes cumulées.   => cumul_PMSS - payslip.cumul_T1 sans RS

T2 sans RS
if SC>SP:
    result = cumul des salaires – cumul PMSS – bases cotisations tranche 2 précédentes. => cumul_BRUT- cumul_PMSS - payslip.cumul_T2 sans RS
else: 
    result =  – base cotisations tranche 2 précédentes cumulées.                        =>   - payslip.cumul_T2 sans RS      #Vérifié   

    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

4 P1
if SC< 4*SP:
cumul_BRUT <= 4 cumul_PMSS => Ce calcul doit être fait en cumulé
SC = cumul_BRUT => result =BRUT+payslip.BRUT 
SP = cumul_PMSS => result =PMSS+payslip.PMSS
4 PMSS cumulés = 4 * SP

cumul_4 P1 sans RS => result =4 P1 sans RS+payslip.4 P1 sans RS 

4 PMSS cumulés = 4 * SP


4 P1 sans RS

if SC  < 4*SP:
    result= cumul salaire – base cotisations 4 P1 précédentes cumulées. => cumul_BRUT- payslip.4 P1 sans RS
else:  
    result = 4 cumul PMSS – base cotisations 4 P1 précédentes cumulées. => 4 * SP - payslip.4 P1 sans RS


Si le salaire annuel cumulé dépasse le montant correspondant à quatre fois le plafond annuel de la Sécurité sociale, 
alors l'abattement est appliqué sur la partie correspondant à quatre fois le plafond annuel, '
puis l'abattement n'est plus appliqué sur la part dépassant ce montant.

salaire brut après abattement: Salaire brut * abattement = salaire brut abattu  = BRUT abattu #if SC > 4*SP:
###=>>>> Dévloppé par DAH ###=>Salarié sur assiette de la CSG et de la CRDS

BRUT abattu =>

if SC < 4*SP:
    result = 4 P1 sans RS * 0.9825 
else :
    result = 4 P1 sans RS * 0.9825 + (T1 sans RS + T2 sans RS - 4 P1 sans RS)

Exemple :

En 2020, le montant correspondant à quatre fois le plafond annuel de la Sécurité sociale est de 164 544 €.

Mon salaire brut annuel est de 165 000 €.

Cela signifie que l'abattement sera appliqué sur le montant de 164 544 €.'

En revanche, l'abattement ne sera pas appliqué sur la partie dépassant ce montant, en d'autres termes 165 000 - 164 544 = 456 €.

Exemple :

J'ai sur mon bulletin un salaire brut de 2 658,55 € et sur mon bulletin je distingue des rubriques de prévoyance et de mutuelle, '
mais pas de rubrique de retraite supplémentaire. Je n'ai également pas d'indemnité de mise à la retraite, de licenciement, d'intéressement ou de participation.'

Les montants patronaux des cotisations prévoyance et mutuelle sont les suivants : 85,50 € et 38,87 €.

Donc, pour calculer l'assiette de la CSG et de la CRDS, je dois procéder de la manière suivante :'

salaire brut = 2 658,55 €. En cumulé, mon salaire annuel est de 33 152,19 €, et donc ne dépasse pas 164 544 €.

On va donc appliquer l'abattement de 1,75 %.'

Salaire brut * abattement = salaire brut abattu

2 658,55 * 98,25 % = 2 612,03 €

Salaire brut abattu + parts patronales des cotisations prévoyance, mutuelle, retraite supplémentaire = assiette de la CSG et de la CRDS

2 612,03 + 85,50 + 38,87 = 2 736,40 €.

L'assiette de la CSG et de la CRDS sera donc de 2 736,40 € sur mon bulletin de salaire.'

###=>>>> Dévloppé par DAH ###=>Salarié sur assiette de la CSG et de la CRDS => COS
Base CSG/CRDS = assiette de la CSG et de la CRDS:

CSG déductible du revenu imposable:         
result = Base CSG/CRDS * 0.068   

CSG non déductible du revenu imposable:
result = Base CSG/CRDS * 0.024   

CRDS non déductible du revenu imposable :          
result =Base CSG/CRDS * 0.005             

Salaire total après déduction de 1.75 % pour frais professionnels(2)  
(2) L’assiette de la déduction forfaitaire pour frais professionnels est limitée à 4 plafonds annuels de sécurité sociale. 
Cette déduction ne s’applique pas à certaines sommes qui ne sont pas à proprement parler du salaire.

déductible de l'impôt sur le revenu. En d'autres termes, cela signifie que le montant ne rentre pas dans l'assiette déclarée chaque année aux autorités fiscales '
afin de calculer le montant à payer au titre de l'impôt sur le revenu.'

non déductible d'impôts. Cela signifie que le montant de la CRDS rentre dans l'assiette servant à calculer le montant à payer au titre de l'impôt sur le revenu.'

Le calcul est le même que ce soit pour l'assiette de la CSG déductible, de la CSG non déductible ou de la CRDS (qui est non déductible également)'



<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'Intégrez les allègements et exonérations   : "Pacte de Responsabilité".'

Les allègements des charges consistent à réduire les cotisations sociales employeurs sur les bas salaires, 
afin d’en abaisser le coût pour les entreprises.

COP

L'objectif est donc de :'

réduire le coût du travail ;

favoriser l'emploi peu qualifié.'

Les allègements de cotisations

La réduction générale des cotisations patronales sur les bas salaires (ex-réduction Fillon)

La réduction « Fillon » est une diminution des charges patronales sur les salaires inférieurs ou égaux à 1,6 fois le SMIC en vigueur.

Le salarié doit remplir certaines conditions pour que cet allègement de charges patronales puisse s'appliquer :'

la rémunération ne doit pas dépasser 1,6 fois le SMIC en vigueur ;

le salarié doit être affilié à l'assurance chômage '
(on exclut donc par exemple les dirigeants de sociétés ayant un statut de mandataire social, les associés égalitaires de SARL, 
les présidents de SAS ou encore les salariés du secteur public, des particuliers employeurs ou des chambres du commerce et de l'industrie, '
de l'agriculture et des métiers) ;'

le contrat de travail du salarié ne doit pas ouvrir droit à une autre exonération de cotisations sociales 
(contrat d'apprentissage ou contrat de professionnalisation conclu avec un demandeur d'emploi de plus de 45 ans, par exemple).

+La rémunération à prendre en compte comprend l'ensemble des éléments soumis à cotisations, '  
=> SC
+la part des cotisations patronales aux régimes de prévoyance et de retraite supplémentaire qui dépassent les limites d'exonération, ' 
=> RS >> cumul_RS == cumul_RS1 + cumul_RS2

+ ainsi que la rémunération des temps de pause, douche, habillage et déshabillage prévue par certaines conventions et accords collectifs étendus.

Concernant le calcul de la rémunération, en 2021 il ne devrait pas dépasser le montant suivant :

35 H * 52 = 1 820 H  => yearly

Pour un salarié à 151,67 => monthly heures/mois : 
1,6 x (10,25 € x 1 820 h) = 29 848 €.

Ce seuil s'apprécie annuellement'

Montant de l’allégement = Rémunération brute mensuelle x coefficient

Coefficient = 0,26/0,6 x ((1,6 * SMIC horaire x nb d’heures rémunérées/Rémunération brute mensuelle)- 1)

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Contrôlez le Smic
Depuis le 1er janvier 2021, le Smic horaire brut est fixé à 10,25 euros. Pour une durée légale de travail de 35 heures hebdomadaires, 
le salaire brut mensuel est porté à 1 554,58 € (soit 151,67 heures x 10,25 euros).

Attention de ne pas confondre le Smic avec le salaire minimum garanti. 
Le minimum garanti est un élément permettant de calculer dans certains cas les avantages en nature, les frais professionnels, etc. 
Il est fixé à 3,65 euros au 1er janvier 2021. Le salaire minimum garanti n’est donc pas un salaire de référence.

Le Smic a un impact sur de nombreuses variables au sein du logiciel de paie, 
comme le calcul de l'allègement généralisé des charges sociales (ex-réduction Fillon) ou le calcul du salaire des alternants. '
C'est pour cette raison qu'il doit être contrôlé.

Le Smic est réévalué minimum une fois dans l'année au 1er janvier. Il peut être rehaussé en cours d'année 
si l'indice des prix à la consommation augmente d'au moins 2 % par rapport à l'indice constaté lors de la mesure du précédent montant du Smic. '
Il augmente dans les mêmes proportions.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
'allègement généralisé des charges sociales (ex-réduction Fillon)'

###=>>>> result = réduction Fillon
###=>>>> Dévloppé par DAH ###=> Employeur sur Totalité du salaire + RS
###=>>>>>cumul_BRUT=> BRUT+payslip.BRUT    sur une base annuelle cumulée,donc de janvier au mois de paie calculé


controle = payslip.Assurance chômage   T1+T2   
a = active = obligatoire 
if 'Assurance chômage T1+ Assurance chômage T2'==a 
controle = payslip.Assurance chômage
if controle:

if 'payslip.Assurance chômage'==active 

cumul_RS1 = RS1 + payslip.cumul_RS1
cumul_RS2 = RS2 + payslip.cumul_RS2
cumul_RS = cumul_RS1 + cumul_RS2
cumul_BRUT => result =BRUT+payslip.BRUT 
cumul_SMIC => result =SMIC+payslip.SMIC 
cumul_PMSS => result =PMSS+payslip.PMSS
cumul_T1 => result =T1+payslip.cumul_T1
cumul_T2 => result =T2+payslip.cumul_T2


if controle:

a = cumul_BRUT
d = cumul_RS
b = cumul_SMIC


    if (a+d)> 1.6*b: 
        result= Pas de réduction Fillon 
    else:  
        result= réduction Fillon 


'Le montant de la réduction ne doit jamais dépasser le montant cumulé des cotisations mentionnées ci-après :'
la cotisation patronale d'assurance maladie'
la cotisation patronale d'assurance vieillesse ; '
la cotisation patronale d'allocations familiales ;'
le Fnal ;
la contribution de solidarité pour l'autonomie ;'
une partie de la cotisation AT/MP (0,78 % en 2019) ;

depuis 2019 : les cotisations patronales Agirc/Arrco et les cotisations d'assurance chômage, mais en deux temps. '
Au 1er janvier 2019, on a donc ajouté les cotisations Agirc/Arrco puis au 1er octobre 2019, 
les cotisations d'assurance chômage, pour la plupart des entreprises. '
Quelques exceptions se sont vu ajouter les cotisations d'assurance chômage dès le 1er janvier 2019.'

'Si le montant calculé dépasse le cumul des cotisations, alors on appliquera le montant du cumul des cotisations mentionnées ci-dessus.'


a=cumul_assurance.maladie => result=assurance.maladie+payslip.cumul_assurance.maladie
b=cumul_COP_assurance.vieillesse_plafonnée => result=assurance.vieillesse_plafonnée +payslip.cumul_assurance.vieillesse_plafonnée 
c=cumul_COP_assurance.vieillesse_deplafonnée => result=assurance.vieillesse_deplafonnée +payslip.cumul_assurance.vieillesse_deplafonnée 
d=cumul_CAF => result =CAF+payslip.cumul_CAF
e=cumul_FNAL_plaf => result =FNAL_plaf+payslip.cumul_FNAL_plaf 
f=cumul_FNAL_deplaf => result =FNAL_deplaf+payslip.cumul_FNAL_deplaf
j=cumul_CSA => result =CSA+payslip.cumul_CSA
h=cumul_AT/MP => result =AT/MP+payslip.cumul_AT/MP
k=cumul_assurance.chômage T1 => result=assurance.chômage T1+payslip.cumul_assurance.chômage T1 
 +cumul_assurance.chômage T2 => result=assurance.chômage T2+payslip.cumul_assurance.chômage T2

l=cumul_COP_Agirc/Arrco 

A =a+b+c+d+e+f+j+h+k+l
R=result = réduction Fillon
if R > A : 
    result= A
else:  
    result= R

min(R,A)

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   
Les exonérations de cotisations
Outre la réduction générale des cotisations patronales sur les bas salaires, 
il existe des exonérations de cotisations sociales possibles en fonction de l’implantation géographique de l’entreprise 
ou du type de contrat de travail du salarié.

Les exonérations ciblées

Exonérations géographiques (liste non exhaustive) :
Exonérations sur des publics prioritaires (liste non exhaustive) : Exemples :
le contrat d’apprentissage ;
le contrat de professionnalisation ;
le contrat unique d’insertion (CUI).

Exonérations sur les services à la personne :
jeunes entreprises innovantes ;
les structures de réinsertion ;
les structures d’insertion par l’activité économique (SIAE) ;
l’exonération « aide à domicile ».

Les exonérations générales:
"""
La modulation de la contribution d'assurance chômage au titre du bonus-malus'

"""
L'idée derrière cette réforme est de motiver les entreprises pour qu'elles embauchent plus de salariés en CDI, ou rallongent la durée des CDD.

La base de calcul sera ce qu'on appelle le taux de séparation ; autrement dit le rapport entre le nombre de fins de contrats de travail ou de missions d'intérim assorties à une inscription à Pôle Emploi, et l'effectif moyen annuel. '

Par la suite, le montant du bonus-malus sera calculé en comparant le taux de séparation de l'entreprise avec le taux de séparation moyen du secteur d'activité concerné.

Le bonus-malus devrait s'appliquer aux entreprises de 11 salariés ou plus à partir du 1er mars 2021.'


"""
La déduction forfaitaire de cotisations patronales pour heures supplémentaires
"""
On désigne également cette exonération sous l'expression déduction forfaitaire patronale.'

Les conditions requises pour en bénéficier sont les suivantes :

être un employeur cotisant à l'assurance chômage ;' if 'payslip.Assurance chômage'==active 

être employeur de salariés des entreprises inscrites au répertoire national des entreprises contrôlées majoritairement par l’État ;

être employeur de salariés relevant soit des établissements publics à caractère industriel et commercial des collectivités territoriales, soit des sociétés d’économie mixte dans lesquelles ces collectivités ont une participation majoritaire, dont l’emploi ouvre droit à l’allocation d’assurance chômage ;

être employeur de salariés relevant des régimes spéciaux de Sécurité sociale des marins, des mines, des clercs et employés de notaire ;

avoir moins de vingt salariés. < 20 ETP

Cette déduction est issue de la loi en faveur du travail, de l’emploi et du pouvoir d’achat (Tepa).

Elle s’applique sur les rémunérations relatives aux heures supplémentaires.

Les heures supplémentaires concernées sont les suivantes :

les heures effectuées au-delà de la durée légale fixée à 35 heures hebdomadaires ;

les heures effectuées au-delà de 1 607 heures pour les salariés titulaires de conventions de forfait en heures sur l’année.

Le montant de la déduction forfaitaire correspond à 1,50 € par heure supplémentaire.

Pour les salariés en forfait jours, elle est de 10,50 € par jour de repos auquel le salarié renonce.

Comme nous l'avons vu, l'effectif de l'entreprise doit être inférieur à 20 salariés. Il s'agit de l'effectif moyen de l'entreprise, au 31 décembre de l'année précédente.'

Si l'entreprise dépasse les 20 salariés en 2016, 2017 ou 2018, la déduction continuera de s'appliquer pendant trois ans.


La déduction forfaitaire ne s'applique pas à :'

l’État, les collectivités territoriales et leurs établissements publics administratifs, scientifiques ou culturels ;

les chambres de commerce et d’industrie, les chambres des métiers et les chambres d’agriculture ;

les particuliers employeurs.

"""
L'exonération des cotisations salariales pour heures supplémentaires, heures complémentaires et jours travaillés au-delà de la limite légale
Mise en place depuis le 1er janvier 2019.
"""

Elle concerne :

Les heures supplémentaires effectuées au-delà de la durée légale de travail.

Les heures complémentaires réalisées par les salariés à temps partiel.

La majoration de rémunération versée aux salariés en forfait jours, en contrepartie du rachat de leurs jours de repos.

La réduction de cotisations salariales portera essentiellement sur les cotisations d'assurance vieillesse et d'assurance veuvage.

À l'origine prévue pour le 1er septembre 2019, cette exonération a été avancée '
pour s'appliquer aux heures mentionnées ci-dessus à partir du moment où elles sont effectuées depuis le 1er janvier 2019.'

Cette exonération pour heures supplémentaires s'accompagne également '
d'une exonération d'impôt sur le revenu limitée à un montant d'heures supplémentaires de 5000 € euros par an. Ce montant correspond à un montant net, '
l'équivalent brut serait donc de 5 358 €. '



================================================================================================================================================================

Cumul imposable (salaire net imposable) : comment est-il calculé ?
15 décembre 2021 par Gestionnaire de paie - Lecture 3 min.
cumul imposable
Le salaire net imposable est à trouver en bas de la fiche de paie des salariés sous la mention « cumul imposable ». 
Il représente la fraction du salaire qui sera assujettie à l’impôt sur le revenu. Il sera la base sur laquelle sera calculé le prélèvement à la source pour la plupart des salariés.

QU’EST-CE QUE LE SALAIRE NET IMPOSABLE ?
Le salaire net imposable est constitué de l’ensemble des rémunérations 
(dont  – IJSS – versées en cas de congés maladie) ayant fait l’objet d’un paiement effectif au cours de l’année d’imposition, 
aux quelles est rajouté la valorisation des avantages en nature éventuellement perçus par le salarié (ex : voiture de fonction). 
il sera différent de l’assiette du prélèvement à la source que dans certains cas particuliers (IJSS, contrats courts, etc.).

Le salaire net imposable est à trouver en bas de la fiche de paye sous la mention « cumul imposable » ou « net imposable ».

CALCUL NET IMPOSABLE
Le cumul imposable est calculé selon la formule suivante :


Salaire net  => :  result = BRUT - categories.SALC or categories.RETENUES
result = Brut - COS  => NET À PAYER AVANT IMPÔT SUR LE REVENU 


Salaire net imposable =>:
result = salaire net + IJSS + avantages en nature + CSG non déductible + CRDS (totalement non déductible) 
+ RF + COP mutuelle T1(totalement réintégré)+COS individuels(mutuelles par exemple)

Montant PAS => or Impôt sur le revenu : taux non personnalisé => :
result = Net imposable or Salaire net imposable * tx 


RF1 = cumul_RF1 - payslip.cumul_RF1
RF2 = cumul_RF2 - payslip.cumul_RF2

RF = RF1 + RF2

+ COP mutuelle T1 :
Complémentaire santé (mutuelle) Tr 1  #=> dites « frais de santé »
cumul_COP mutuelle T1   =  COP mutuelle T1 + payslip.cumul_COP mutuelle T1

Le salaire imposable est net, car les cotisations sociales obligatoires ou complémentaires en sont déduites. 
Mais il est différent de la somme que touchera le salarié à la fin du mois (le net à payer).

En revanche, certains éléments à la charge de l’employeur constituent des avantages pour le salarié et doivent réintégrer le net imposable du salarié. 
C’est le cas des mutuelles et cotisations patronales dites « frais de santé » qui viennent augmenter l’assiette de l’impôt sur le revenu. 
Elles sont identifiée sur la fiche de paie par la ligne « Réintégration fiscale ».

NB : les cotisations facultatives ou versées au titre de contrats individuels souscrits sur l’initiative du salarié, comme les mutuelles, ne sont pas déductibles du salaire imposable.
=> COS individuels(mutuelles par exemple)

DÉDUCTIBLE OU NON DÉDUCTIBLE ?
Le terme « déductible » signifie que cette cotisation vient diminuer le salaire brut pour en déterminer le net à payer. 
Lorsqu’une cotisation est « non déductible », elle vient de même diminuer le salaire brut afin d’en déterminer le net à payer mais est prise en compte pour le net imposable.

Depuis le 1er janvier 2018, certaines charges salariales ont disparues au profit d’une augmentation de la CSG. En conséquence, la CSG déductible est à prendre en compte dans la limite de 6,80 %.

Quant à la CRDS (0,5 %), la totalité est non déductible.

En 2022, la limite de déductibilité fiscale des prévoyances complémentaires et retraites supplémentaires est fixée à :

+ 5% du plafond annuel de la sécurité sociale 
+ 2% de la rémunération annuelle,

ne pouvant excéder 2 % de 8 fois le PASS pour la prévoyance complémentaire à caractère collectif et obligatoire

8% de la rémunération annuelle brute dans la limite de 8 PASS pour la retraite supplémentaire.
Par ailleurs les apprentis bénéficient d’une exonération d’impôts sur les revenus perçus en 2021 en dessous de 18 760€. 
Les stagiaires sont eux-aussi exonérés d’impôts sur les gratifications de stage au titre de 2021 dans la limite du Smic annuel. 
Pour la déclaration d’impôt à effectuer l’année prochaine, la limité à prendre en compte sera le SMIC annuel 2022.

==================================================================================================================================================================

cumul jours travaillés        = payslip.cumul_joules indemnités de mise à la retraite, de licenciement ou de départ volontaire dans le cadre d’un plan social, pour la partie qui excède les montants conventionnels ou légaux ;rs+JrTravailParMois      #cumul_nbr_jrs

Cumul Régul IR jours présence = payslip.cumul_regul_jr_ir + regul_jr_ir   # cumul_regul_jr_ir c'est le nombre de jour cumulé de PRESENCE effective 

cumul jours absences          = absence_cumulee = cumul_nbr_jrs - cumul_regul_jr_ir

# il faut donc donc retrancher aussi le nombre de jour de regul d'ir (payslip.regul_jr_ir) dans le cas d'une régularisation
# JrTravailParMois = le nombre de jour légaux de travail par mois (généralement 26)
# payslip.cumul_jours = le nombre de jour legaux de travail cumulé en fin de mois précédent (généralement 26 x m-1)
# payslip.regul_jr_ir = le nombre de jour d'absence du mois impactant l'IR
# regul_jr_ir=JrTravailParMois - payslip.regul_jr_ir        PRESENCE effective du mois
# payslip.cumul_regul_jr_ir = le nombre de jour cumulé de PRESENCE effective en fin de mois précédent 
    
    if payslip.regul: 
        presence_theorique_cumulee = payslip.cumul_jours + JrTravailParMois
        absence_cumulee = (payslip.cumul_jours - payslip.cumul_regul_jr_ir) + payslip.regul_jr_ir
        presence_reelle_cumulee = presence_theorique_cumulee - absence_cumulee => cumul_regul_jr_ir =>Cumul Régul IR jours présence

payslip.sal_journalier= BASE/26
rub.montant*payslip.sal_journalier
payslip.duration= Abscence
result = -payslip.duration*BASE/26
esult=-payslip.duration* prime_caisse/26
-rub.montant*IndRep/26


if payslip.rubriques_ids:
    for rub in payslip.rubriques_ids: 
        if rub.name.code=='rappel_salaire_jrs':  
            result=rub.montant*payslip.sal_journalier
            break 
        else: 
            result=0
else: 
    result=0 

if payslip.rubriques_ids:
    for rub in payslip.rubriques_ids: 
        if rub.name.code=='regul_ind_represent_v':  
            result=-rub.montant*IndRep/26
            break 
        else: 
            result=0
else: 
    result=0 


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Plafonds tranches effectifs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Depuis le 1er avril 2021, l’administration considère que le plafond ne doit plus être proratisé (ni pour temps partiel, ni pour absence non rémunérée, etc.) 
(voir FH 3888, §4-25). 
Les entreprises ont pu choisir d’appliquer cette nouvelle doctrine dès le 1er avril, pour les déclarations sociales faites au titre de l’année 2021.

À noter

À partir de 2022, la règle sera obligatoire (BOSS, Assiette générale, §§ 1180 et 1190, 01/04/2021).


"""
PLAFOND :
"""
On peut noter quatre catégories de cas particuliers en termes d ajustement du plafond mensuel de la Sécurité sociale :

Ajustement du plafond mensuel au prorata temporis.

La réduction du plafond en cas d absence.

La réduction du plafond en cas de travail à temps partiel.

Le versement de sommes pendant une période de suspension du contrat de travail sans rémunération.

1° L'Ajustement du plafond mensuel au prorata temporis: 2 CAS: Les salariés non mensualisés et les salariés travaillant à la pièce.'

les travailleurs saisonniers ou les intermittents, il faut qu'ils soient payés au moins deux fois par mois, et avec maximum 16 jours d'intervalle.

alors le calcul applicable sera le suivant : 

=valeur mensuelle du plafond de la période de paie x nombre de jours de la période d’emploi / nombre de jours calendaires de la période.

Calcul PMSS PASS ANNEE TRIMESTRE MOIS QUINZINE SEMAINE JOUR HEURE 
Code             PMSS 
Type de montant  Montant fix

Quantité         1.0

Montant fixe     3428  


pour les salariés travaillant à la pièce et qui seraient rémunérés à la quinzaine, 

le plafond est égal à 50 % du plafond mensuel de la Sécurité sociale, soit 1 714 € en 2020.
Code             PMSS*50% 
Type de montant  Montant fix

Quantité         1.0

Montant fixe     3428*0.5

2°La réduction du plafond en cas d'absence :'

entrée ou sortie en cours de mois ;

contrat ne couvrant pas une période de paie ;

absence non rémunérée qui ne donne pas lieu à maintien de salaire ;

périodes d activité partielle indemnisée 

absence pour congés payés, lorsque le paiement des congés payés est assuré par une caisse de compensation.

Les absences inférieures à la journée ne donnent pas lieu à réduction du plafond. 
C'est le cas par exemple d'une demi-journée de grève ou d'une heure d'absence non rémunérée.

Le calcul :

valeur mensuelle du plafond * nombre de jours de la période d emploi / nombre de jours calendaires du mois.

Un salarié quitte l'entreprise le 13 février 2020 :'
valeur mensuelle du plafond * nombre de jours de la période d emploi / nombre de jours calendaires du mois

Soit 3 428 * 13 / 29 = 1 536,69 €.

Un salarié prend des congés sans solde du 6 au 10 avril 2020.

Le plafond :

valeur mensuelle du plafond * nombre de jours de la période d emploi / nombre de jours calendaires du mois

Soit 3 428 * 25 / 30 = 2 856,67 €.

Plafond*rub.montant /30                          rub.montant = nombre de jours de la période d'emploi'

Plafond*regul_jr_ir /JrTravailParMois(30)        regul_jr_ir = nombre de jours de la période d'emploi'

#regul_jr_ir=JrTravailParMois - payslip.regul_jr_ir        PRESENCE effective mensuelle

# JrTravailParMois = le nombre de jour theorique de travail par mois Soit 31 30 29 28  (Maroc généralement 26)

nombre de jours calendaires du mois

Code             JrTravailParMois(30)
Type de montant  Montant fix

Quantité         1.0

Montant fixe     30 

3°La réduction du plafond pour 'un salarié à temps partiel'

Le calcul :
valeur mensuelle du plafond x (durée contractuelle du travail + heures complémentaires / durée légale du travail ou conventionnelle si elle est inférieure).

Exemple :

Un salarié travaille 130 heures sur le mois de juin 2020. Il n'a pas d'heures complémentaires sur ce mois.

Son plafond :

valeur mensuelle du plafond x durée contractuelle du travail / durée légale du travail ou conventionnelle si elle est inférieure

Autrement dit :

3 428 * 130 / 151,67 = 2 938,22 €.

durée légale du travail ou conventionnelle => nombre de heures/mois

Code             heures_theorique/mois
Type de montant  Montant fix

Quantité         1.0

Montant fixe     151,67 

Cette réduction de plafond ne va pas s appliquer aux salariés :

qui ne sont pas à temps partiel au sens du Code du travail (forfait jours, par exemple) ;

pour lesquels sont appliqués des taux spécifiques, des assiettes ou des montants de cotisations forfaitaires ;

qui travaillent régulièrement et simultanément pour le compte de plusieurs employeurs ;

intérimaires des entreprises de travail temporaire ;

en activité partielle indemnisée.


4°'Le versement de sommes pendant une période de suspension du contrat de travail sans rémunération :'

Si un salarié reçoit des éléments variables de rémunération alors que son contrat est suspendu, 
alors les cotisations sont calculées sur la base des taux et plafonds de la dernière période de travail.

En revanche, si la dernière période remonte à une année précédant celle de versement de l élément de rémunération, 
alors on admet que les taux et plafonds appliqués sont ceux de l'année de versement de l'élément de rémunération.

Exemple :

Un salarié est en congé sans solde depuis le 1er juillet 2019.

Il reçoit en janvier 2020 une prime de résultat due au titre du mois de mai 2019.

Comme son contrat est suspendu depuis le 1er juillet 2019, il n'est pas possible de rattacher cette prime à la dernière période d'emploi ; 
on appliquera donc les taux et plafonds de l année de versement, soit de janvier 2020.

<<<<<<<<<<<<<<<<<

Depuis 2019
Suite à l'unification de l'Agirc et de l'Arrco, on abandonne la référence aux catégories de cotisant '
et on reprend au sein du régime Agirc-Arrco les droits et obligations de chaque branche,autour de deux tranches de cotisations.

Une tranche 1 limitée au  (PMSS) : soit 3 428€ en 2020. => T1

Une tranche 2 allant de 3 428 € à 8 PMSS, soit un maximum de 27 424 € en 2020. =>  8 P1 or ( 8 P1 - T1 ) #or T2  

Ces deux tranches s'appliquent pour les cadres et les non-cadres.'

les tranches  :
cumul_BRUT => result =BRUT+payslip.BRUT 
cumul_PMSS => result =PMSS+payslip.PMSS
cumul_T1 => result =T1+payslip.cumul_T1
cumul_T2 => result =T2+payslip.cumul_T2


Depuis le 1er janvier 2019, suite à la fusion des deux caisses de retraite complémentaire AGIRC ARRCO, tout a été simplifié. 
Depuis cette date, seules deux tranches de salaire restent en vigueur pour tous les salariés, cadres et non-cadres.

Tranche 1 : les cotisations pour un salaire allant de 0 euros à 3 428 euros, soit 1 fois le plafond (PMSS) ;
Tranche 2 : pour un salaire brut allant de 3 428 euros jusqu’à 27 424 euros, soit 8 fois le PMSS.

 => Moins

Si le cumul des salaires est > au cumul PMSS, alors :

la tranche 1 = cumul PMSS – base cotisations tranche 1 précédentes cumulées.
La tranche 2 = cumul des salaires – cumul PMSS – bases cotisations tranche 2 précédentes.

Si le cumul des salaires est < au cumul PMSS, alors :

la tranche 1 = cumul salaire – base cotisations tranche 1 précédentes cumulées.
la tranche 2 =  – base cotisations tranche 2 précédentes cumulées.


Il faut donc chaque mois comparer le cumul des rémunérations avec le cumul des plafonds

T1
    if SC<SP:cumul_BRUT<cumul_PMSS
result= cumul salaire – base cotisations tranche 1 précédentes cumulées.=cumul_BRUT-payslip.cumul_T1
    else:  
result = cumul PMSS – base cotisations tranche 1 précédentes cumulées.=cumul_PMSS-payslip.cumul_T1

T2
    if SC>SP:cumul_BRUT>cumul_PMSS
result = cumul des salaires – cumul PMSS – bases cotisations tranche 2 précédentes.=cumul_BRUT-cumul_PMSS-payslip.cumul_T2
    else: 
result =  – base cotisations tranche 2 précédentes cumulées.=-payslip.cumul_T2


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Les effectifs: "effectif moyen".
se calcule en faisant la moyenne du nombre de personnes employées chaque mois de l'année civile précédente. '

"neutralisation des franchissements de seuils d'effectif "

Calcul de l’effectif annuel

Salariés pris en compte pour la détermination de l’effectif moyen
Sont pris en compte :
les salariés titulaires d’un contrat de travail y compris ceux dont le contrat de travail est suspendu ;
les fonctionnaires et agents non titulaires des 3 fonctions publiques ;
les salariés des entreprises inscrites au RNECME (répertoire national des entreprises contrôlées majoritairement par l'État) ;'
les fonctionnaires d’Orange, les salariés des IEG.

Les personnes sont à inclure dans les effectifs de l'établissement qui a l'obligation de les inscrire à son registre unique du personnel (RUP).

Les employeurs auxquels l'obligation d'établir un RUP ne s'applique pas doivent néanmoins procéder au décompte comme s'ils étaient soumis à cette obligation.

Prise en compte de la durée de travail et du temps de présence sur le mois

Les salariés ou agents à temps plein ou complet, présents tout le mois, sont décomptés pour 1.

Les mandataires sociaux également titulaires d'un contrat de travail comptent uniquement pour 1.'

Les salariés en forfaits jours comptent pour 1 quel que soit le nombre de jours de leur forfait inférieur à 218.

Les salariés à temps partiel ou non complet, sont pris en compte au prorata 

en divisant:la somme totale des horaires inscrits dans leurs contrats de travail/la durée légale ou la durée conventionnelle du travail.

Les salariés en forfaits heures peuvent faire l'objet du même prorata.'

Embauche/débauche en cours de mois

le décompte est effectué à due proportion du nombre de jours du mois de la présence effective ; il est donc tenu compte du nombre de jours calendaires.

nombre de jours de la période d'emploi / nombre de jours calendaires du mois'

rub.montant /31                          rub.montant = nombre de jours de la période d'emploi'

regul_jr_ir /JrTravailParMois(31)        regul_jr_ir = nombre de jours de la période d'emploi'

#regul_jr_ir=JrTravailParMois - payslip.regul_jr_ir        PRESENCE effective mensuelle

# JrTravailParMois = le nombre de jour theorique de travail par mois Soit 31 30 29 28  (Maroc généralement 26)

nombre de jours calendaires du mois

Code             JrTravailParMois(31)
Type de montant  Montant fix

Quantité         1.0

Montant fixe     31 

Les deux modalités de décompte - temps partiel et embauche/débauche - s'appliquent cumulativement'

Exemple : un salarié embauché le 20 janvier = 12/31 soit 0,4.

Si la personne est à temps plein, elle sera comptabilisée en janvier pour 0,4 = (1 x 0,4).

Si la personne a un contrat de travail de 24 heures hebdomadaire, 

elle sera comptabilisée en janvier pour 0,27 = (24/35 x 12/31) si la durée légale est appliquée dans l'entreprise.'

result = la somme totale des horaires inscrits dans leurs contrats de travail/la durée légale ou la durée conventionnelle du travail.

result = durée contractuelle du travail / durée légale du travail ou conventionnelle si elle est inférieure

Autrement dit :

durée légale du travail ou conventionnelle => nombre de heures/semaine

Code             heures_theorique/Hebdomadaires
Type de montant  Montant fix

Quantité         1.0

Montant fixe     35 

Comment faire le décompte ?

Pour calculer l'effectif global et l'effectif moyen, il faut opérer un décompte.

Le calcul de l'effectif mensuel prend en compte tous les salariés titulaires d'un contrat de travail le dernier jour de chaque mois,y compris les salariés absents. 

Le calcul de l'effectif annuel est établi au niveau de l'entreprise tous établissements confondus 

result = la moyenne des effectifs de chaque mois de l'année N - 1 (effectif moyen annuel). '

Les personnes sont décomptées d'après le nombre de jours pendant lesquels elles ont été employées.'

Exemple : une entreprise a eu une activité saisonnière du 01/05/2017 au 31/10/2017, avec 11 salariés en mai et octobre, 15 en juin, et 23 en juillet, août et septembre.

result = L'effectif est égal à : (11 + 15 + 23 + 23 + 23 + 11) / 6 = 17,666, soit 17,66 salariés.'

Effectif global:

Pour calculer l'effectif global, il faut prendre en compte le nombre de salariés présents dans l'entreprise au 31 décembre.

Chaque salarié compte pour une unité, quelles que soient la durée et les conditions de travail.

Effectif moyen annuel en ETP (équivalent temps plein)

Pour calculer l'effectif moyen annuel, il faut tout d'abord calculer l'effectif moyen mensuel pour chaque mois de l'année.

L'effectif moyen mensuel est calculé en nombre d'ETP (équivalent temps plein).

Un ETP est une unité de mesure proportionnelle au nombre d'heures travaillées par un salarié sur un an.'

Exemple :

1 salarié à mi-temps sur 12 mois = 0,5 ETP.

2 salariés à mi-temps sur 12 mois = 1 ETP (0,5 ETP x 2)

1 salarié à temps plein sur 6 mois = 0,5 ETP

L'équivalent temps plein (ETP) est calculé à partir de la durée mensuelle légale de travail, égale à 151,67 heures.'

À savoir : la durée mensuelle légale de travail, égale à 151,67 heures, est une moyenne rapportée à l'année,'
elle diffère donc de la durée de 35 heures hebdomadaires multipliée par 4 semaines. 
Elle est calculée de la façon suivante : 35 heures hebdomadaires x 52 semaines = 1 820 heures pour l'année, '
ce qui fait 1 820 h/12 mois = 151,67 heures par mois.

Exemple d'effectif moyen mensuel en ETP pour un mois donné'

Nombre de salariés à retenir dans le calcul = nombre d'ETP'

10 CDI à temps complet  => 10 ETP

2 CDI à temps partiel ayant travaillé chacun 65 heures : 65 h x 2 /151,67 h = 0,86 => 0,86 ETP

1 CDD à temps complet pour augmentation d'activité présent au cours des 12 derniers mois => 1 ETP'

1 CDD de 6 mois à 100 heures par mois => 6 mois/12 mois x (100 heures / 151,67 heures) = 0,32 ETP => 0,32 ETP

1 apprenti => 0 ETP 

Effectif du mois 12,18 ETP

Ce calcul doit être fait pour chaque mois de l'année.'

Ensuite, il faut calculer la moyenne des effectifs mensuels au 31 décembre, en additionnant le nombre d'ETP et en le divisant par 12 mois.'

Donc, l'effectif moyen annuel est égal à 118,86 ETP divisé par 12 mois soit 9,90 ETP. Le chiffre est arrondi au centième le plus proche.'

Pour une entreprise créée en cours d'année, '

il faut faire la somme des effectifs mensuels depuis la création d'entreprise jusqu'au 31 décembre et diviser par le nombre réel de mois.

En fin d'année, l'employeur doit indiquer les effectifs de son entreprise sur la déclaration sociale nominative (DSN).

Attention : les mois au cours desquels aucun salarié n'est employé ne sont pas pris en compte dans le calcul de l'effectif moyen. 
Par exemple, si aucun salarié n'est embauché durant le mois de juin, il faut diviser la somme des effectifs mensuels par 11 (et non 12).'



<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
GTA 
Dans un premier temps, il faut préciser que les méthodes de calcul utilisées en paie viennent de la pratique et non des textes de lois en vigueur.

Par conséquent, il existe énormément de méthodes de calcul possibles. Il a donc fallu que la jurisprudence intervienne, par le biais de la Cour de cassation, 
afin de définir certains principes permettant de réglementer l utilisation des méthodes de calcul existant dans le domaine de la paie.

'Les principes de base'
Avant de nous attaquer aux calculs de base de la paie, nous allons nous intéresser à certains éléments spécifiques qui vont nous aider à comprendre et à maîtriser ces calculs. 
Ainsi, cela va nous permettre d accroître nos compétences de gestionnaires de paie.

'La base horaire du salarié'

Le fait que le salarié ait une base horaire en heures ou en jours vient influer directement sur le choix de la méthode de calcul à utiliser.

En effet, le décompte de l absence ne se fait bien sûr pas de la même manière selon la nature de cette base horaire ; 
et que ce soit pour des raisons de logique, de continuité ou encore de simplification, 
il est nécessaire dappliquer un calcul en jours pour un salarié en forfait jours, ou en heures pour un salarié travaillant en heures.

'Les jours ouvrés'
Il s agit tout simplement des jours de la semaine pendant lesquels le salarié travaille, donc classiquement du lundi au vendredi, 'soit cinq jours.'

'Les jours ouvrables'
Pour calculer une absence sur la base des jours ouvrables, 'on compte les jours du lundi au samedi.'

'Les jours calendaires'
Le concept de jour calendaire est facile à définir et comprendre : il s agit de tous les jours de la semaine, ou du mois, 
selon la période dont est déduite l absence, y compris les jours fériés et les week-ends.

En d autres termes, 'les jours calendaires vont du lundi au dimanche.'

Cette méthode est différente de la méthode de calcul dite "aux trentièmes", en ce que cette dernière n est basée que sur 30 jours, 
tandis que la méthode de calcul en jours calendaires dépend du nombre de jours dans le mois.

Les "jours moyens" ou les "heures moyennes"
Cette méthode consiste à retenir un nombre spécifique, indifféremment du mois concerné ou encore du nombre de jours ou d''heures travaillés par le salarié.

Exemple :

Le nombre de jours moyen mensuel est généralement 21,67, parfois arrondi à 22.

Le nombre d''heures moyen dans un mois est de 151,67 heures.

Il faut inclure les jours fériés dans les différents calculs, comme étant des jours travaillés.

Les méthodes de calcul de l''absence:

Il existe huit méthodes de calcul pour décompter l absence sur le bulletin de paie, toutes découlant de la pratique et non de la législation.

Ces méthodes de calcul concernent toutes les absences, sauf les congés payés et la maladie qui font lobjet de réglementations bien spécifiques. 
En effet, il s'agit ici d'absences qui suspendent le contrat de travail, et donc l'obligation pour l'employeur de verser un salaire en contrepartie.

Il s'agit par exemple des absences suivantes' :

congé sans solde ;

absence injustifiée ;

entrée ou sortie des effectifs de l'entreprise en cours de mois.'

Dans le cas des congés payés et de la maladie, ce sont des absences qui sont assimilées à du travail effectif 
et pour lesquelles l'employeur continue de verser un salaire en contrepartie, par le biais d'indemnités.

Une seule méthode sur toutes celles qui existent est reconnue par la Cour de cassation, à savoir la méthode de "calcul au réel". (Cass. soc. 11 février 1982, n°80-40359, BC V n°90).

En conséquence, par rapport à ce que nous disions plus haut sur l'impact de la base horaire du salarié sur la méthode de calcul utilisée, '
cela signifie que les deux méthodes suivantes vont pouvoir s'appliquer' :

la méthode de calcul de l'absence en heures réelles pour les salariés travaillant en heures ;'

la méthode de calcul de l'absence en jours réels pour les salariés travaillant en jours.'

Cela étant dit, il reste possible d'utiliser une autre méthode de calcul que la méthode "au réel", si et seulement si cela reste plus favorable pour le salarié !'

Elle a notamment été retenue pour les cas suivants :

congé sans solde ;

maladie non indemnisée ;

entrée en cours de mois (Cass. soc. 14-5-1987 n° 1967) ;

sortie en cours de mois (Cass. soc. 20-1-1999 n° 388) ;

retenues pour heures de grève (Cass. soc. 19-5-1998 n° 2450).

Quelle que soit la méthode utilisée par l'entreprise pour calculer les éléments de paie, il faut que cette méthode soit utilisée pour tous les salariés de l'entreprise sans exception.

Avant de passer à l'illustration de ces méthodes de calcul, il faut noter que maintenant l'entrée ou la sortie dans le mois ne se calculent plus par le biais d'une déduction d'absence,
mais simplement en proratisant le salaire de base par un calcul au réel.

Nous allons maintenant nous pencher sur ces différentes méthodes.

Dans les exemples donnés ci-dessous afin d'illustrer les différents calculs proposés, nous reprendrons le même scénario, à savoir :'

Un salarié avec un salaire de base mensuel de 3 500 €, absent du 6 au 10 janvier 2020. Il travaille 35 heures par semaine.

Pour les exemples qui vont être utilisés, nous partons du principe que seul le salaire de base du salarié est utilisé pour le calcul de l'absence.'

Le calcul de l'absence au réel'

Comme son nom l'indique, cette méthode prend en compte ce qu'on appelle les heures réelles, soit les heures véritablement travaillées par le salarié, 
ainsi que les heures pendant lesquelles il a véritablement été absent.

'En heures réelles ':

Il y a 23 jours ouvrés en janvier, donc 23 * 7 heures de travail par jour = 161 heures réelles en janvier. Le salarié est absent une semaine, soit 5 jours ouvrés, donc un total de 5*7 = 35 heures.
Pour trouver le montant de la déduction, il faut donc diviser le salaire de base par la totalité des heures travaillées en janvier, puis le multiplier par le nombre d'heures d'absence.

(3 500/161) * 35 = 760,87€

En jours réels :

Il y a 23 jours ouvrés en janvier. Le salarié est absent une semaine, soit 5 jours ouvrés. Pour trouver le montant de la déduction, 
il faut donc diviser le salaire de base par la totalité des jours ouvrés en janvier, puis le multiplier par le nombre de jours d absence.

(3 500/23) * 5 = 760,87 €

Le calcul de l'absence moyenne'
En "heures moyennes" :

Comme expliqué précédemment, il y a 151,67 heures en moyenne dans un mois. En revanche, le nombre d'heures à déduire pour le salarié reste 35 heures.'

(3 500/151,67) * 35= 807,67 €

En "jours moyens" :

Il y a en moyenne 21,67 jours dans un mois, mais cela peut être arrondi à 22. C est cette base qui sera utilisée dans notre exemple. 
On divisera donc le salaire de base par 22 puis on multipliera le résultat par le nombre exact de jours d'absence du salarié, soit 5 jours.'

(3 500/22) * 5 = 795,45 €

Le calcul de l'absence en jours ouvrables':

En jours ouvrables réels :

En janvier 2020, il y a exactement 27 jours ouvrables, soit 23 jours ouvrés et 4 samedis. On va donc, pour cette méthode, 
diviser le salaire de base par 27 avant de le multiplier par le nombre de jours ouvrables d'absence du salarié, autrement dit 5 jours ouvrés et un samedi, donc un total de 6 jours ouvrables.'

(3 500/27) * 6 = 777,78 €

En "jours ouvrables moyens" :

La moyenne des jours ouvrables dans un mois est de 26. On va donc reprendre le principe du calcul ci-dessus, mais en remplaçant 27 par 26 jours ouvrables.

(3 500/26) * 6 = 807,69 €

Le calcul de l'absence en jours calendaires':

En jours calendaires réels :

Il y a 31 jours calendaires en janvier. Le salarié est absent une semaine, soit 7 jours calendaires. Pour trouver le montant de la déduction, 
il faut donc diviser le salaire de base par la totalité des jours calendaires en janvier, puis le multiplier par le nombre de jours calendaires d'absence.'

(3 500/31) * 7 = 790,32 €

En "jours calendaires moyens" :

Le nombre de "jours calendaires moyens" est de 30. Le salarié est absent une semaine, soit 7 jours calendaires. Pour trouver le montant de la déduction, 
il faut donc diviser le salaire de base par la totalité des "jours calendaires moyens" en janvier, puis le multiplier par le nombre de jours calendaires d'absence.'
(3 500/30) * 7 = 816,67 €


Résumé:

en J & H reeles  ouvrés

3500*5/23  3500*(5*7)/(23*7)  760,87€

en J & H  moyenne  

3500*5/22 795,45 € 3500*(5*7)/(151,67)     807,67 €


en J ouvrables REELS

3500*6/27      777,78 €

en J ouvrables MOYENNES

3500*6/26       807,69 €


en J CALENDIARES REELS

3500*7/31     790,32 €

en J CALENDIARES MOYENNES

3500*7/30 816,67 €

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

"""
Parametrez-votre-logiciel-de-paie
"""
Il existe deux formes de logiciels de paie :

les logiciels de paie en monoposte qui sont exploités sous licence et installés sur les ordinateurs de l’entreprise ou sur le réseau informatique. 
On peut citer quelques exemples comme Isapaye, Cegid, Sage ou encore Pegase ;

les logiciels de paie en mode SaaS (Software As A Service) dont la solution est installée dans les serveurs de l'éditeur. '
Parmi quelques exemples de logiciels en mode Saas, on peut citer Silæ ou encore PayFit.

Voici une liste non exhaustive des principales fonctions d’un logiciel de paie :

collecte des éléments variables des bulletins de paie ;

édition des bulletins de paie des salariés ;

télédéclaration des déclarations sociales nominatives (DSN) ;

réalisation des documents d'entrée comme la DPAE (déclaration préalable à l'embauche), le contrat de travail ;

réalisation des documents de sortie comme l’attestation Pôle Emploi, le certificat de travail, le reçu pour solde de tout compte ;

édition de tableau de bord de reporting ;

édition des écritures de paie dans la comptabilité ;

tenue du registre du personnel ;

dématérialisation des bulletins, et archivage légal.
"""
Configurez les paramètres communs à tous les logiciels de paie
Décomposez un logiciel de paie
"""

Pour cela, le paramétrage du logiciel de paie est un élément clé. Un logiciel de paie comporte trois types de paramètres concernant :

l’entreprise ;

les salariés ;

le plan de paie.


Le plan de paie permet notamment de gérer les cotisations salariales et patronales, le net imposable, la CGS-CRDS, le Smic, le plafond de la Sécurité sociale, 
les congés payés, etc. Tous ces éléments permettent la bonne production des bulletins de paie. Bien que le plan de paie soit largement automatisé, 
il reste des paramètres à mettre en place ou à contrôler.
"""
Découvrez les différents modèles de bulletins
"""
Le modèle de bulletin est un type de bulletin qui regroupe des caractéristiques, comme les cotisations sociales, en fonction des particularités de l’entreprise et du salarié. 
Il permet d’appliquer les bonnes cotisations sociales, puisque le modèle est prédéfini

Les modèles de bulletins sont donc déterminés par le statut du salarié. Parmi eux, on retrouve les modèles de bulletins de paie basiques comme : 

le modèle cadre ;

le modèle non-cadre ;

le modèle du contrat de professionnalisation ;

le modèle alternant ;

le modèle apprenti (contrat d’apprentissage) ;

le modèle stagiaire.

À noter que les stagiaires ne sont pas assimilés à des salariés. Un stagiaire doit avoir un bulletin de paie si sa gratification est supérieure au minimum légal. 
On parle alors de modèle de bulletin du stagiaire. 
Si la rémunération du stagiaire n'est pas supérieure au minimum légal, il n'a pas de bulletin.

Pour déterminer le bon modèle de bulletin, les caractéristiques suivantes sont à prendre en compte :

le type de contrat :

contrat à durée indéterminée (CDI),

contrat à durée déterminée (CDD) ;

l’effectif de l’entreprise ;

les heures du contrat de travail :

la mensualisation,

le forfait jours,

le forfait heures,

les heures supplémentaires.

Prenons l’exemple d’un salarié non-cadre qui travaille 169 heures par mois. Nous connaissons deux des quatre éléments nécessaires pour déterminer le modèle de bulletin :

le statut du salarié : non-cadre ;

le nombre d’heures de contrat : mensualisation pour 169 heures dans le mois.

Afin de déterminer son modèle de bulletin, il nous faut connaître deux éléments complémentaires :

le type de contrat ;

l’effectif de l’entreprise.

Dans cette entreprise, l’effectif est inférieur à 20 salariés. Le salarié a un contrat en CDI. Dans ce cas, notre salarié aura le modèle de bulletin dans le logiciel de paie suivant : 
modèle de bulletin non-cadre 169 h en CDI dont l’effectif est de moins de 20 salariés.
"""
En résumé
"""
Un logiciel de paie est un outil informatique qui permet de gérer l’ensemble du processus de ressources humaines, de l'entrée jusqu'à la sortie du salarié, 
en passant par les démarches administratives. 

Un logiciel de paie ne se limite pas à la production des bulletins.

Le logiciel de paie est ainsi composé de trois types de paramètres :

l’entreprise ;

les salariés ;

le plan de paie.

Le plan de paie permet notamment de gérer les cotisations salariales et patronales, le net imposable, la CGS-CRDS, le Smic, le plafond de la Sécurité sociale, les congés payés, etc. 

Le modèle de bulletin est un type de bulletin qui regroupe des caractéristiques, comme les cotisations sociales, en fonction des particularités de l’entreprise et du salarié. 
"""
Préparez le dossier client dans votre logiciel de paie
Créez un nouveau dossier
"""
On parle de création d’un dossier client lorsque l’entreprise recrute pour la première fois des salariés.

Il ne faut pas confondre création d’un dossier client et création d’une entreprise.

Tout dossier client est composé au minimum des rubriques suivantes :

le dossier de l’entreprise ;

le dossier des salariés.
"""
Créez le dossier de l’entreprise
"""
Afin de faciliter le paramétrage du logiciel de paie, vous devez collecter en amont un certain nombre de documents et d’informations auprès de l’entreprise.

Ils peuvent se résumer sous la check-list entreprise suivante.

1- Les documents juridiques 
Le Kbis, qui sert à justifier de l'activité commerciale d'une entreprise ou d'une société.'

L'avis Siren, qui permet de rechercher une entreprise ou un établissement au sein du répertoire d'identification des entreprises et de leurs établissements.

Les statuts de la société, qui matérialisent ses principales caractéristiques, notamment ses objectifs et son fonctionnement général vis-à-vis des associés ou actionnaires, et des tiers).

Le contrat de prévoyance.

Le contrat de mutuelle.

Attention à ne pas confondre numéro Siren et avis Siren. Le numéro Siren peut se retrouver dans l’avis Siren.

2- Les documents administratifs
Le RIB de l’entreprise.

La carte d'identité des associés et des mandataires sociaux.'

Le taux d’accident du travail.

Le contrat d'adhésion à la médecine du travail.'

Cette liste n’est pas exhaustive, et dépend également des pratiques internes.

Certains documents comme le contrat d'adhésion à la médecine du travail ou le taux d’accident du travail ne sont pas nécessairement disponibles lors du paramétrage du logiciel. '
Il faudra compléter par la suite le dossier client.

Le taux d’accident du travail est communiqué tous les débuts d'année par la Carsat à l’entreprise.' 

Une fois le dossier de l’entreprise constitué, les dossiers salariés doivent être complétés.

Créez le dossier salariés
Les documents à collecter pour chaque salarié sont les suivants.

1- Les documents juridiques 
Le contrat de travail.

Le contrat individuel de retraite supplémentaire.

Le contrat individuel de mutuelle.

Le contrat individuel de prévoyance.

2- Les documents administratifs 
La carte d'identité du salarié.'

La carte Vitale du salarié.

La déclaration préalable à l’embauche (DPAE) du salarié.

Le RIB du salarié.

Tous les documents constituant le dossier client s’accompagnent d’informations à valider ou de questions.

Réalisez l’audit du dossier client lors d’une création de dossier client
Tout dossier client doit faire l’objet d’un contrôle en amont.

À quoi sert le contrôle ? 

Le contrôle s’effectue au niveau des documents remis par le client, afin d’en assurer la conformité au niveau juridique. 
ll permet également de poser des questions au client en cas d'incohérences ou d’erreurs. Il permet surtout de corriger les éléments faux, '
afin d’avoir une base correcte pour la création du paramétrage du logiciel de paie.

C’est une étape très importante à ne pas négliger, notamment lors de la reprise d’un dossier client.

Quels sont les points à contrôler ? 

Parmi les contrôles qui peuvent être réalisés, on peut citer :

la détermination des organismes collecteurs ;

le choix de la convention collective applicable ;

la vérification de l'implantation de l’entreprise dans une zone permettant l'exonération de cotisations sociales ou non.

Cette liste n’est pas exhaustive. 

Vous avez besoin d’un rafraîchissement de mémoire concernant la notion d’organismes collecteurs ? Rendez-vous dans le cours Apprenez à lire un bulletin de paie.

Ce contrôle est à compléter par des questions à poser directement à l’entreprise. En effet, 
l’analyse seule des documents présents dans le dossier client ne permet pas d’identifier de façon complète : 

les aides possibles ;

les cotisations complémentaires ;

les exonérations de cotisations.

Or, ces éléments sont indispensables pour un paramétrage optimal du logiciel de paie.

Voici une liste non exhaustive de questions à poser à l’entreprise afin de valider le paramétrage du logiciel de paie, et d’assurer le respect de la législation :

Le président de SAS se rémunère-t-il via un bulletin de paie ?

Le salarié n’ayant pas souhaité adhérer à la mutuelle entreprise vous a t-il remis un courrier de renonciation à la mutuelle ?

Quel est le jour prévu pour la journée de solidarité ?

Les salariés ont-ils un lien de parenté avec le mandataire social ?

Certains de vos salariés sont-ils inscrits à Pôle Emploi ?

Avez-vous un local dans lequel vos salariés peuvent manger à la pause du midi ?

Quels sont les horaires de travail de l’entreprise ?
"""
Reprenez un dossier client
Reprenez le dossier entreprise
"""
On parle de reprise de dossier lorsqu’un dossier de paie est traité soit par un prestataire externe de type cabinet d’expertise comptable, soit par le client en interne.

Lors de la reprise d’un dossier, le dossier se compose des documents de base pour la création d’un dossier, auxquels s’ajouteront d’autres documents.

L’entreprise ayant un historique de salariés, et des salariés présents dans l’entreprise, la collecte des anciens documents permet de paramétrer convenablement le logiciel de paie.

Voici la liste des documents complémentaires à renseigner lors de la reprise d'un dossier client :'

les déclarations sociales nominatives (DSN) des 3 dernières années ;

le calculs des effectifs des 3 dernières années ;

le registre du personnel ;

les usages de l’entreprise (c'est-à-dire les avantages accordés librement et de manière répétée par un employeur à ses salariés, sans que le Code du travail, '
une convention ou un accord collectif ne l'impose) ;'

les accords d’entreprise ;

le règlement intérieur de l’entreprise ;

les rescrits sociaux ;

les derniers jugements prud’homaux ;

les 6 derniers contrôles Urssaf.

Certains éléments mentionnés dépendent de l’effectif de l’entreprise, comme par exemple les accords d’entreprise ou encore le règlement intérieur.

Reprenez le dossier salariés
Les documents demandés lors de la création du dossier salarié sont complétés par les éléments suivants :

les bulletins de paie des 3 dernières années ;

le solde des congés payés de l'année en cours et de l'année précédente ;

les provisions de congés payés de l'année en cours et de l'année précédente ;

le(s) nom(s) du/des membre(s) du comité social et économique (CSE).

Il est préférable de mettre trop d’informations au moment du paramétrage du logiciel de paie, que pas assez.

Les documents demandés sont nombreux et parfois non nécessaires au paramétrage du logiciel de paie, 
mais permettent d’anticiper les éventuels contrôles Urssaf. Ces derniers peuvent avoir lieu sur les 3 dernières années.

Pour en savoir plus, vous pouvez consulter le cours Anticipez un contrôle Urssaf.

Le paramétrage est à penser de façon globale. Il doit permettre d'utiliser l’outil à son maximum, d’automatiser tout ce qui est possible de l'être, 
et d'anticiper les bulletins de paie futurs.'

Auditez la reprise du dossier client
La reprise d’un dossier client (entreprise et salariés) dans le logiciel de paie est plus technique que la création d’un dossier client, 
car il y a davantage de points à contrôler, comme nous allons le voir.

Un audit plus poussé que pour la création d’un dossier client doit alors être réalisé.

Qu’est-ce que l’audit de reprise ?

L’audit de reprise vise à faire l’état des lieux des pratiques de paie afin de détecter et de corriger des anomalies. 
Il permettra notamment de mettre les pratiques de l’entreprise en conformité avec le droit du travail et la convention collective.

L’audit de reprise du dossier client se décompose en quatre étapes.

 1- La collecte des données 
Il s’agit des documents à collecter, que nous avons vus précédemment au cours de ce chapitre.

 2- L’analyse des documents
Elle permet de faire l'état des lieux de la pratique en paie en auditant les bulletins de paie et les pratiques en matière de droit du travail.'

3- La validation ou la non-validation des incohérences
L’analyse des données peut mettre en évidence des incohérences qu’il faudra éclaircir avec le client. 
Il peut par exemple s’agir d’un salarié présentant une mutuelle famille sur son bulletin de paie, alors qu’il est célibataire.

4- La rectification des anomalies
À l’issue des questions posées au client, des anomalies peuvent apparaître. Elles doivent être mentionnées au client le plus rapidement possible, 
et surtout rectifiées sur le bulletin de paie du mois suivant.

La collecte des informations et leur contrôle prennent du temps, mais restent nécessaires pour limiter les erreurs et produire des bulletins de paie justes et respectant la réglementation.

C’est pour cette raison que les documents sont à demander bien avant la première production des bulletins de paie. Un planning de création ou de reprise de dossier peut être réalisé en ce sens.


En résumé


Le dossier client est composé au minimum des rubriques suivantes :

le dossier de l’entreprise ;

le dossier des salariés.

Le dossier salariés doit contenir les documents administratifs et juridiques des salariés.

Lors d'une reprise de dossier, il est indispensable de récupérer : '

les bulletins de paie des 3 dernières années ;

le solde des congés payés de l'année en cours et de l'année précédente ;

les provisions de congés payés de l'année en cours et de l'année précédente ;

le(s) nom(s) du/des membre(s) du comité social et économique (CSE).

Question 1
À quoi sert un logiciel de paie ?

Contrairement aux idées reçues, le logiciel de paie ne permet pas seulement de créer des bulletins, ou de créer des bulletins en cliquant sur un bouton. 
Cela permet de gérer l’ensemble du processus de ressources humaines, de l'entrée jusqu'à la sortie du salarié, en passant par les démarches administratives. 

Question 2
Quelles sont les principales fonctionnalités du logiciel de paie ?

Le logiciel de paie ne sert pas seulement à la production des bulletins de paie. Voici une liste non exhaustive des principales fonctions d’un logiciel de paie, 
hors production des bulletins de paie :

télédéclaration des déclarations sociales nominatives (DSN) ;
réalisation des documents d'entrée, comme la DPAE, le contrat de travail ;'
réalisation des documents de sortie comme l’attestation Pôle Emploi, le certificat de travail, le reçu pour solde de tout compte ;
édition de tableau de bord de reporting ;
édition des écritures de paie dans la comptabilité ;
tenue du registre du personnel ;
dématérialisation des bulletins, et archivage légal.

Question 3
Quels sont les paramètres de base à mettre en place au sein du logiciel de paie ?


Le paramétrage d'un logiciel de paie est complet lorsque trois types de paramètres sont réalisés : '

le paramétrage de l’entreprise ;
le paramétrage des salariés ;
le paramétrage du plan de paie.

Question 4
Quelle est la première étape lors du paramétrage du logiciel de paie ?

Prendre connaissance du dossier client.
Le paramétrage du logiciel de paie intervient uniquement après la prise de connaissance du dossier client, qui doit être complet. 
Le dossier client permet de regrouper tous les documents et informations utiles au bon paramétrage du logiciel de paie.

Question 5
Que permet de gérer le plan de paie ?

Le plan de paie permet notamment de gérer les cotisations salariales et patronales, le net imposable, la CSG-CRDS, le Smic, le plafond de la Sécurité sociale, etc. 

La date de départ des salariés est gérée directement dans le paramétrage des salariés. 

Question 6
De quoi est composé le dossier client permettant le paramétrage du logiciel de paie ?

Le dossier client est composé d’une partie concernant l’entreprise et d’une partie concernant les salariés. Chacun des documents a été collecté en amont et contrôlé, 
afin de valider les éléments de la paie. Pour fluidifier la paie, certains ont été mis sous format de check-list ou de fiche navette.

Question 7
Quelle est l'étape la plus importante au moment de la reprise d’un dossier client ?'


Auditer le dossier client lors d’une reprise, tout comme lors d’une création de dossier, est essentiel. Cette étape permet de sécuriser le paramétrage du logiciel de paie. 

Question 8
Lors de la création d’un nouveau dossier client, quels sont les éléments à collecter concernant l’entreprise ?

On privilégie la collecte des documents administratifs et juridiques des salariés et de l’entreprise. Sur ces documents, 
on collectera les informations permettant le paramétrage du logiciel de paie. On retrouvera ainsi le numéro Siret sur l’extrait Kbis, par exemple.


Paramétrez les données de l’entreprise



Paramétrez le logiciel en fonction des spécificités de votre entreprise

En résumé

Le paramétrage de l’entreprise comprend en partie l’aspect administratif. 

Toutefois, il ne faut pas oublier les paramétrages spécifiques à compléter avec soin : l’effectif de l’entreprise des 3 dernières années, les conventions collectives applicables, la journée de solidarité, les jours fériés, le calendrier de l’entreprise,  les méthodes de calcul des absences et des congés payés. 

Il convient également de renseigner les différents organismes collecteurs de l’entreprise comme la Sécurité sociale, la retraite complémentaire, la mutuelle ou encore la prévoyance.

Le paramétrage du logiciel de paie s'étend au-delà du paramétrage actuel, il se doit d'anticiper, afin de limiter le temps de production des bulletins de paie, par exemple


Paramétrez le plan de paie

""""
Paramétrez les tickets restaurant
"""
Qu'est-ce qu'un ticket restaurant ?

La participation patronale est exonérée de cotisations et d'impôt sur le revenu si :'

Le montant est compris entre 50 % et 60 % de la valeur du titre.

Le montant ne dépasse pas une valeur forfaitaire par titre-restaurant : en 2020, cette valeur a été fixée à 5,55 €.

Les titres restaurant, appelés également tickets restaurant, chèques déjeuner ou encore pass restaurant, sont un titre de paiement qui permet au salarié de payer son repas.

Les titres restaurant sont remis aux salariés des entreprises qui ne disposent pas de cantine, d’une salle de restauration aménagée pour pouvoir déjeuner, ou qui ne versent pas de prime déjeuner.

Le titre restaurant est financé par l’employeur entre 50 % et 60 % de sa valeur. Le salarié reçoit un ticket restaurant par jour travaillé.

Prenons un exemple. Un salarié travaille à temps plein du lundi au vendredi. Il prend 5 jours ouvrés de congés payés dans le mois. Sachant que le mois de mars comporte 22 jours ouvrés.

###=>>>> Dévloppé par DAH ###=> Employeur sur les tickets restaurant 
result = jours_ouvres_mensuel = nbre_jours_ouvrés du mois => 22 J
result = jours_ouvres_conges_mensuel   = nbre_jours_conges_ouvrés du mois => 5 J
result = 17 jours (22 jours – 5 jours de congés) => Nbre_ticket_restaurant_effectif

Combien aura-t-il de tickets restaurant pour le mois de mars ?

Le salarié a travaillé 17 jours (22 jours – 5 jours de congés). Comme le salarié reçoit un ticket-restaurant par jour travaillé (jours ouvrés), il percevra donc 17 tickets restaurant.

La valeur faciale du titre restaurant ouvrant droit à l'exonération maximale est comprise entre 9,25 euros et 11,10 euros.'

Les tickets restaurant sont exonérés de cotisations sociales lorsque la contribution patronale ne dépasse pas 5,55 euros pour les titres 2021 (11,10 euros x 50 %).

###=>>>> Dévloppé par DAH ###=> Employeur sur les tickets restaurant
limite du plafond = (11,10 euros x 50 % ) = 5,55

Si la contribution de l'employeur dépasse cette limite, la fraction de la contribution excédant le plafond légal est réintégrée dans l'assiette des cotisations sociales de l'entreprise.'

Prenons un exemple. 

Un salarié perçoit 17 tickets restaurant au cours d’un mois donné. La valeur faciale d’un ticket restaurant est de 15 euros. L’entreprise prend en charge 55 % du ticket restaurant, soit 8,25 euros.

Le ticket restaurant est en partie exonéré de cotisations sociales pour un montant de 5,55 euros (limite du plafond). Le delta de 2,70 euros par ticket restaurant rentre dans la base des cotisations sociales.

Ainsi, le montant du ticket restaurant soumis à cotisation sera de 17 tickets x 2,70 euros = 45,90 euros.

Le salaire du mois étant de 2 500 euros, la base de cotisation déplafonnée sera de 2 545,90 euros.


###=>>>> Dévloppé par DAH ###=> Employeur sur les tickets restaurant
ticket restaurant = 17  =>  Nbre_ticket_restaurant_effectif
prise en chareg COP = 55 % du ticket restaurant, soit 8,25 euros.=> result = valeur_faciale * tx_ pris en charge_cop
c'est entre Le titre restaurant est financé par l’employeur entre 50 % et 60 % de sa valeur'
valeur_prise en chareg COP = 15 * 55 %  = 8,25
limite du plafond = (11,10 euros x 50 % ) = 5,55

RS_ticket_restaurant_mensuel = (valeur_prise en chareg COP - limite du plafond) * Nbre_ticket_restaurant_effectif = (8,25 - 5,55) * 17 = 2,70 * 17 = 45,90

###=>>>> Dévloppé par DAH ###=> Employeur sur les tickets restaurant

a = valeur_prise en chareg COP #=> valeur_faciale * tx_ pris en charge_cop
b = limite du plafond   # => (11,10 euros x 50 % ) = 5,55
c = Nbre_ticket_restaurant_effectif # => 
#result = jours_ouvres_mensuel = nbre_jours_ouvrés du mois => 22 J
#result = jours_ouvres_conges_mensuel   = nbre_jours_conges_ouvrés du mois => 5 J
#result = 17 jours (22 jours – 5 jours de congés) => Nbre_ticket_restaurant_effectif

if a > b :
    result = (a-b)*c

else :
    result = 0

# Le delta de (a-b) euros par ticket restaurant rentre dans la base des cotisations sociales.
# Ainsi, le montant du ticket restaurant soumis à cotisation sera de c tickets x (a-b)euros = 45,90 euros.
RS_ticket_restaurant_mensuel = cumul_delta TR - payslip.cumul_delta TR 
cumul_delta TR = RS_ticket_restaurant_mensuel + payslip.cumul_delta TR


RS => cumul_RS == cumul_RS1 + cumul_RS2 + cumul_delta TR


"""
En résumé
Le paramétrage du plan de paie contient plusieurs éléments, et notamment les lignes et taux de cotisations spécifiques.

Une couverture minimale santé est obligatoire depuis le 1er janvier 2016 dans toutes les entreprises employant des salariés.

L'employeur doit proposer une mutuelle à tous les salariés, y compris aux apprentis.

Dans le logiciel de paie, la mutuelle doit être saisie.

D’autres cotisations doivent également être renseignées, comme les tickets restaurant et la retraite supplémentaire.

"""
Ajoutez les informations des salariés
"""

En résumé
Le paramétrage du logiciel de paie peut sembler facile en raison de l’ergonomie des logiciels récents. Pourtant, la gestion de la paie reste l’application du droit du travail.

Le paramétrage du logiciel de paie sera plus poussé pour les reprises de dossiers clients que pour les créations de dossiers clients.

Le paramétrage du logiciel de paie s'effectue grâce aux éléments collectés dans le cadre de la constitution du dossier client, et à l’issue d’un audit.

Le paramétrage du logiciel de paie est complet s’il présente le paramétrage de l’entreprise, des salariés et du plan de paie.

Le logiciel de paie doit être automatisé le plus possible, afin de permettre l'édition rapide et sans erreur des bulletins de paie et autres documents administratifs.

"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Toutes les étapes du cycle de paie sont listées
En résumé

Le calendrier de traitement de la paie :
•   date limite d'envoi des données ;'
•   date limite d'envoi des bulletins pour validation '
•   date limite de clôture de la paie.

La priorisation des tâches
•   Une notification de fin de contrat, quel que soit le motif, est absolument prioritaire !
•   En période de traitement de paie, les données relatives à cette paie sont plus urgentes que des questions d'ordre général qu'un client pourrait vous poser.
•   Des éléments de rémunération communiqués en retard par rapport à la date limite doivent normalement pouvoir attendre le mois suivant, surtout si cela crée un risque de retard au niveau du traitement de la paie.
Revoyez l’intégralité des informations communiquées par votre client ou les RH
 Cela signifie que :
•   si vous percevez la moindre incohérence dans les informations communiquées ;
•   si des données sont incomplètes ;
•   s'il vous manque des informations,'

La finalité de l'élément de rémunération'
•   Il faut bien analyser la nature de l'élément pour en déterminer le calcul applicable.'

La vérification dans l'historique de paie'
Vérifier le paramétrage des rubriques utilisées
Savoir où chaque élément de rémunération doit apparaître sur le bulletin
Éléments soumis à cotisations
Total du brut
Cotisations sociales
Éléments non soumis à cotisations sociales, donc nets
Salaire net
Optimiser les saisies manuelles
•   Il faut privilégier les imports de données, afin de gagner du temps et d'éviter les erreurs de saisie manuelle.'

•   L'étape du contrôle est essentielle dans le cadre du processus de paie.'
•   Vérifiez les cumuls des données communiquées par le client.
•   Contrôlez les autres modifications demandées, une par une.
•   Toujours vérifier les alertes déclenchées par le logiciel.
•   Contrôler les consignes enregistrées dans le logiciel, afin de s'assurer de la conformité des saisies avec les spécificités des salariés et/ou de l'entreprise.
•   Certaines données demandent une vérification systématique.
•   Apprenez à vérifier les plafonds et cotisations sociales rapidement.
•   Un nouveau salarié ou une fin de contrat doivent faire l'objet d'un contrôle plus détaillé, minutieux et méthodique.
•   Sachez analyser les erreurs, de façon à pouvoir les expliquer et à les empêcher de se reproduire.


Tous ces éléments réunis vont vous permettre de calculer correctement 
Exemple :
Un nouveau salarié vient d'être embauché. Sa fiche d'embauche indique :
•   un contrat d'apprentissage ;'
•   une qualification "employé" ;
•   une catégorie de cotisant "stagiaire".
Aucune de ces informations n'est cohérente avec les deux autres. Il est donc indispensable de revenir vers votre contact pour lui demander de vous confirmer ces trois éléments et, le cas échéant, de corriger la fiche d'embauche.
Exemples :
•   un départ à la retraite peut être à l'initiative de l'employeur ou du salarié. Les règles d'exonération de cotisations sociales de l'indemnité ne sont pas les mêmes selon le cas de figure ;
•   une fin de contrat pendant la période d'essai fera l'objet de règles spécifiques, selon que c'est l'employeur ou le salarié qui met fin à la période d'essai ;
•   le pourcentage appliqué aux heures supplémentaires dépend du nombre d'heures effectuées sur la même semaine, donc les dates auxquelles les heures ont été travaillées sont un élément essentiel que le client doit communiquer.
Exemple :
Si votre salarié est en arrêt maladie, vous allez devoir vérifier les informations suivantes :
•   La convention collective dont il dépend ;
•   son ancienneté au sein de l'entreprise ;'
•   son statut, c'est-à-dire s'il est cadre ou employé ;
•   le nombre de jours calendaires de maladie qui vous a été communiqué ;
•   s'il a eu des absences maladie plus tôt dans l'année civile et si oui, combien de jours elles ont duré.

Tous ces éléments réunis vont vous permettre de calculer correctement l'arrêt maladie sur le bulletin de paie.'
De façon plus régulière, il vous faudra toujours contrôler le salaire brut mais aussi la catégorie de cotisant du salarié, de façon à déterminer si les cotisations suivantes sont calculées avec le bon taux :
1.  Cotisation assurance maladie maternité invalidité décès : est-ce que le salaire brut est supérieur à 2,5 SMIC (sur une base annuelle cumulée, donc de janvier au mois de paie calculé) ? Si oui, on applique un taux de 13 %, sinon de 7 %.
2.  Contribution allocations familiales : est-ce que le salaire brut est supérieur à 3,5 SMIC (sur une base annuelle cumulée, donc de janvier au mois de paie calculé) ? Si oui, on applique un taux de 3,45 % ainsi qu'un taux additionnel de 1,80 %, sinon on applique seulement un taux de 3,45 %. 
3.  Contribution d'équilibre technique : est-ce que le salaire est supérieur au PMSS (sur une base annuelle cumulée, donc de janvier au mois de paie calculé) ? Si oui, alors on applique le calcul de la cotisation depuis le début. Sinon, on ne la calcule pas sur le bulletin. 
4.  Cotisation APEC : est-ce que le salarié dépend des articles 4 et 4bis de la convention collective nationale de 1947 ? Si oui, on calcule la cotisation sur le bulletin tous les mois. 

Exemple :
Il peut arriver qu'un salarié soit soumis à ce qu'on appelle la "saisie arrêt" ou "saisie sur salaire". En quelques mots, il s'agit d'une retenue de salaire opérée par les autorités fiscales directement sur le bulletin du salarié, par le biais de son employeur. Cela signifie que l'employeur va déduire un certain montant net, qu'il va ensuite reverser aux autorités fiscales.
La règle d'or concernant le calcul de cet élément est qu'il faut bien évidemment qu'il reste en fin de mois au salarié de quoi subvenir à ses besoins mais aussi à ceux de sa famille, plus précisément des personnes "à charge", c'est-à-dire qui dépendent de lui.
Typiquement, cela concerne les enfants, mais parfois cela peut être un membre de la famille qui ne peut pas subvenir à ses propres besoins.
Le nombre de personnes à charge va aider à déterminer le montant qui pourra être déduit du salaire net de l'employé.'
Cela signifie que si le montant de la saisie sur salaire est trop important, elle devra se faire sur plusieurs mois, en fonction à chaque fois du salaire net mensuel et du nombre de personnes à charge.

Exemples :
•   congés supplémentaires pour ancienneté ;
•   heures supplémentaires ;
•   travail le week-end et les jours fériés ;
•   la maladie, la maternité et la paternité ;
•   les règles de calcul pour l'indemnité de licenciement ;'
•   la prime d'ancienneté.'
Il faut généralement appliquer la règle la plus favorable.
Donc si, et il s'agit du cas de figure le plus courant, les dispositions de la convention collective sont plus favorables que celles du Code du travail, il faut impérativement les appliquer.

Si ces accords internes ou ces usages sont moins favorables que les dispositions légales ou conventionnelles, il faudra alors alerter votre client ou votre contact au sein de votre entreprise : il n'est pas légal de les appliquer en paie.
Il s'agit par exemple des absences suivantes :'
•    congé sans solde ;
•   absence injustifiée ;
•   entrée ou sortie des effectifs de l'entreprise en cours de mois.'

Elle a notamment été retenue pour les cas suivants :
•   congé sans solde ;
•   maladie non indemnisée ;
•   entrée en cours de mois (Cass. soc. 14-5-1987 n° 1967) ;
•   sortie en cours de mois (Cass. soc. 20-1-1999 n° 388) ;
•   retenues pour heures de grève (Cass. soc. 19-5-1998 n° 2450).

Quelle que soit la méthode utilisée par l'entreprise pour calculer les éléments de paie, il faut que cette méthode soit utilisée pour tous les salariés de l'entreprise sans exception.

Proratisation des éléments de rémunération
Ainsi, ces méthodes de calcul vont très souvent servir à proratiser des éléments de calcul, en cas d'absence du salarié.'
Cela concerne essentiellement des éléments qui sont liés à la notion de travail effectif du salarié.
Parmi ces éléments, on peut noter entre autres :
•   indemnité véhicule ;
•   indemnité télétravail ;
•   prime d'assiduité ;'
•   acquisition des RTT ;
•   acquisition des congés payés.
De même, le principe est toujours celui de l'application de la méthode la plus favorable au salarié, autrement dit qui le pénaliserait le moins en termes de montant déduit, ou bien réduirait le moins possible son acquisition de jours de congés.
La finalité de l'élément de rémunération'
Exemple :
Votre client vous indique un remboursement des frais de repas dans les données mensuelles. Cet élément n'avait encore jamais été passé en paie pour ce client. Cela vient d'être mis en place de leur côté.

Seule ombre au tableau, vous n'arrivez pas à identifier de manière précise l'élément concerné. Alors oui, vous savez que cela concerne des frais de repas, mais cela peut se présenter de différentes manières :
•   indemnité de repas ;
•   frais de repas professionnels ;
•   prime de panier ;
•   tickets-restaurant.
La vérification dans l'historique de paie'
Exemple :
Vous avez un nouveau salarié à intégrer dans le logiciel de paie ce mois-ci.
•   Son salaire est de 5 000 € brut.
•   Votre contact vous indique que la qualification de ce salarié est "employé" et que sa catégorie de cotisant est "article 4 de la convention collective nationale de 1947".
•   Sa base horaire est en heures mensuelles, soit 151,67 heures.
Ces différents éléments doivent vous amener à vous interroger sur la cohérence des informations qui vous ont été communiquées.
En effet, le salaire est plutôt élevé et correspond au salaire de quelqu'un qui aurait une qualification "cadre" et non "employé".'
En vérifiant auprès d'un autre salarié du même établissement, vous remarquez que ce dernier a une base horaire en forfait jours (218 jours sur l'année) et une qualification "cadre".
À partir de ce constat, vous décidez d'envoyer un mail à votre contact afin de confirmer avec lui ces différents éléments.'

Il n'est donc pas possible d'appliquer un mode de calcul différent entre deux salariés.
En cas de report des jours de congés acquis non pris d'une année sur l'autre, l'entreprise doit appliquer le même nombre de jours de congés à reporter pour tous les salariés, sans exception.


Confirmer les composants de son calcul
Exemple :
Une prime, un bonus ou une commission vous seront très souvent communiqués sous forme de montant seulement.
Dans ce cas, les rubriques concernées doivent être paramétrées de façon à ce qu'en saisissant le montant de la prime, du bonus ou de la commission, celui-ci aille directement se reporter au niveau du montant, et non de la base de la rubrique, par exemple.
Cela peut paraître simpliste et même évident présenté comme cela, mais cela peut arriver. 

Exemple :
Des primes ou des bonus trimestriels peuvent être calculés à partir d'éléments tels que le salaire de base, la prime d'ancienneté ou encore les heures supplémentaires.
Cela signifie que ces éléments devront être paramétrés dans le logiciel de paie au niveau de la base.


Il y a également des salariés dont la fonction ou la situation impliquent une paie spéciale qui nécessite d'aller chercher certaines informations bien spécifiques, ou encore des variables de paie avec des éléments à contrôler à chaque fois.
Exemples :
•   un salarié en situation de contrat de reclassement nécessite de vérifier la durée de son congé, et surtout, si celle-ci dépasse la durée du préavis qu'il aurait normalement dû effectuer. En effet, à partir du moment où la durée du préavis est dépassée, alors le salarié ne perçoit plus que 65 % de la rémunération brute moyenne des 12 derniers mois précédant la notification du licenciement, sans qu'elle puisse être inférieure à 1 273,70 € ;
 
•   un stagiaire doit depuis 2014 être payé en fonction des heures réelles effectuées chaque mois, et non plus de manière forfaitaire. Cela implique de recalculer le montant chaque mois en fonction des heures travaillées ;
 
•   les indemnités kilométriques, versées au salarié lorsqu'il utilise son véhicule personnel afin d'effectuer des déplacements pour son activité professionnelle, nécessitent de vérifier la limite d'exonération des cotisations sociales fixée par le barème fiscal.


Ainsi, si nous prenons l'exemple du fameux salaire de référence nécessaire pour calculer l'indemnité de congés payés selon la méthode du dixième, il faut un paramétrage spécial, prenant en compte d'autres éléments que le salaire de base ; comme par exemple :
•   commissions ;
•   heures supplémentaires ;
•   absences.
Cela signifie que le paramétrage de ces rubriques doit absolument inclure leur intégration dans le calcul du salaire de référence.





Dans la théorie, les tranches de salaire doivent être régularisées annuellement. En pratique, c’est différent. Les bulletins de salaire étant réalisés tous les mois, il est plus courant de suivre cette régularisation mensuellement. La rémunération d’un salarié peut varier d’un mois à l’autre, c’est pourquoi il est plus sûr de réaliser le suivi chaque mois. S’il est vrai que le logiciel en paie s’occupe de tous ces calculs, il est vivement conseillé de savoir le réaliser soi-même. Vous n’êtes pas à l’abri d’une coquille de la part de ce dernier.


Ainsi, si nous prenons l'exemple du fameux salaire de référence nécessaire pour calculer l'indemnité de congés payés selon la méthode du dixième, il faut un paramétrage spécial, prenant en compte d'autres éléments que le salaire de base ; comme par exemple :
1.  commissions ;
2.  heures supplémentaires ;
3.  absences.
4.  

Exemples :
•   un salarié en situation de contrat de reclassement nécessite de vérifier la durée de son congé, et surtout, si celle-ci dépasse la durée du préavis qu'il aurait normalement dû effectuer. En effet, à partir du moment où la durée du préavis est dépassée, alors le salarié ne perçoit plus que 65 % de la rémunération brute moyenne des 12 derniers mois précédant la notification du licenciement, sans qu'elle puisse être inférieure à 1 273,70 € ;
 
•   un stagiaire doit depuis 2014 être payé en fonction des heures réelles effectuées chaque mois, et non plus de manière forfaitaire. Cela implique de recalculer le montant chaque mois en fonction des heures travaillées ;
 
•   les indemnités kilométriques, versées au salarié lorsqu'il utilise son véhicule personnel afin d'effectuer des déplacements pour son activité professionnelle, nécessitent de vérifier la limite d'exonération des cotisations sociales fixée par le barème fiscal.
Il peut également exister des situations impactant la vie des salariés, comme par exemple un arrêt maladie ou un congé maternité, qui vont nécessiter de vérifier les paies des mois précédents, afin de confirmer le nombre de jours déjà alloués au titre de ces arrêts, et de vérifier combien peuvent être maintenus par la convention collective dont dépend le salarié, ainsi que le pourcentage du salaire qui sera maintenu.

•   Vous vous en doutez, chacun de ces éléments, même s'il a pour finalité la prise en charge des repas des salariés, n'a absolument pas le même traitement en paie, et peut même concerner des événements différents.
•   Ainsi, les tickets-restaurant vont forcément couvrir les frais de repas pris par le salarié lui-même de façon quotidienne, tandis que les remboursements de frais professionnels vont couvrir des repas à nature normalement exceptionnelle, impliquant souvent des déplacements professionnels et des rendez-vous en clientèle.
•   Les règles ne seront donc pas les mêmes, non plus que les données qui devront être communiquées.
•   Pour ce qui est des tickets-restaurants, le gestionnaire de paie aura donc par exemple besoin du nombre exact de tickets-restaurants alloués au salarié chaque mois, ainsi que la répartition employeur/employé du montant du ticket.
•   En revanche, pour les remboursements des frais de repas, il faudra le montant net exact dépensé par le salarié.
•   D'où l'importance de pouvoir faire la distinction entre chacun de ces éléments, et de pouvoir les expliquer correctement à votre client afin de récupérer les informations nécessaires.
Exemples :
•   un avantage en nature est soumis à cotisations sociales, mais le même montant est déduit avant le salaire net, afin de ne pas être versé au salarié ;
•   les primes, commissions et bonus sont soumis à cotisations sociales, même s'il est possible de voir parfois des primes au net, par exemple ;'
•   une indemnité kilométrique n'est pas soumise à cotisations, tandis qu'une indemnité logement ou véhicule le sera ;
•   les remboursements de frais professionnels sont un remboursement exact du montant dépensé par le salarié, donc non soumis à cotisations sociales. On dit alors que c'est un montant net de cotisations sociales.


Exemple :
Un nouveau salarié vient d'être embauché. Sa fiche d'embauche indique :
•   un contrat d'apprentissage ;'
•   une qualification "employé" ;
•   une catégorie de cotisant "stagiaire".
Aucune de ces informations n'est cohérente avec les deux autres. Il est donc indispensable de revenir vers votre contact pour lui demander de vous confirmer ces trois éléments et, le cas échéant, de corriger la fiche d'embauche.


 Exemples :
•   un départ à la retraite peut être à l'initiative de l'employeur ou du salarié. Les règles d'exonération de cotisations sociales de l'indemnité ne sont pas les mêmes selon le cas de figure ;
•   une fin de contrat pendant la période d'essai fera l'objet de règles spécifiques, selon que c'est l'employeur ou le salarié qui met fin à la période d'essai ;'
•   le pourcentage appliqué aux heures supplémentaires dépend du nombre d'heures effectuées sur la même semaine, donc les dates auxquelles les heures ont été travaillées sont un élément essentiel que le client doit communiquer.


Exemple :

Exemples :
•   congés supplémentaires pour ancienneté ;
•   heures supplémentaires ;
•   travail le week-end et les jours fériés ;
•   la maladie, la maternité et la paternité ;
•   les règles de calcul pour l'indemnité de licenciement ;'
•   la prime d'ancienneté.'

Il faut généralement appliquer la règle la plus favorable.


•   indemnité de repas ;
•   frais de repas professionnels ;
•   prime de panier ;
•   tickets-restaurant.


Vous vous en doutez, chacun de ces éléments, même s'il a pour finalité la prise en charge des repas des salariés, n'a absolument pas le même traitement en paie, et peut même concerner des événements différents.
Ainsi, les tickets-restaurant vont forcément couvrir les frais de repas pris par le salarié lui-même de façon quotidienne, tandis que les remboursements de frais professionnels vont couvrir des repas à nature normalement exceptionnelle, impliquant souvent des déplacements professionnels et des rendez-vous en clientèle.
Les règles ne seront donc pas les mêmes, non plus que les données qui devront être communiquées.
Pour ce qui est des tickets-restaurants, le gestionnaire de paie aura donc par exemple besoin du nombre exact de tickets-restaurants alloués au salarié chaque mois, ainsi que la répartition employeur/employé du montant du ticket.
En revanche, pour les remboursements des frais de repas, il faudra le montant net exact dépensé par le salarié.
D'où l'importance de pouvoir faire la distinction entre chacun de ces éléments, et de pouvoir les expliquer correctement à votre client afin de récupérer les informations nécessaires.

.


Savoir où chaque élément de rémunération doit apparaître sur le bulletin
La présentation du bulletin était donc, dans la plupart des cas car il n'y avait pas vraiment de règles, la suivante :'
éléments soumis à cotisations
total du brut
cotisations sociales
éléments non soumis à cotisations sociales, donc nets
salaire net
Désormais, des éléments non soumis à cotisations sociales, comme par exemple le remboursement des frais de transport ou les tickets-restaurant, se trouvent en haut de bulletin, au même titre que les éléments soumis à cotisations sociales.
Il est donc important de pouvoir catégoriser les éléments, selon qu'ils seront ou non soumis à cotisations sociales.'
Exemples :
•   un avantage en nature est soumis à cotisations sociales, mais le même montant est déduit avant le salaire net, afin de ne pas être versé au salarié ;
•   les primes, commissions et bonus sont soumis à cotisations sociales, même s'il est possible de voir parfois des primes au net, par exemple ;'
•   une indemnité kilométrique n'est pas soumise à cotisations, tandis qu'une indemnité logement ou véhicule le sera ;
•   les remboursements de frais professionnels sont un remboursement exact du montant dépensé par le salarié, donc non soumis à cotisations sociales. On dit alors que c'est un montant net de cotisations sociales.


l'import automatique des données dans le logiciel de paie.'

Vérifiez les cumuls
Dans un premier temps, nous allons nous intéresser ici à ce que nous entendons par "cumuls".
Il s'agit tout simplement des totaux de chaque donnée de paie communiquée par votre client interne ou externe.'
Exemple :
•   le nombre total de congés payés pris par les salariés du client sur le mois en cours ;
•   le montant total des commissions versées aux salariés du client.


L'avantage en nature véhicule ne peut pas être proratisé.'
La commission est généralement directement liée au résultat du travail effectif du salarié et intégrée directement dans le contrat de travail, contrairement à la prime qui peut très souvent avoir un caractère exceptionnel.
Une commission ou une prime est forcément soumise à charges sociales, donc doit figurer au niveau du brut. En revanche, un remboursement de frais professionnels se fera systématiquement en net.

Afin de faciliter les contrôles de ce bulletin d'embauche, je vous propose une liste la plus exhaustive possible des différents éléments à contrôler absolument :'
•   salaire de base (le prorata en cas d'entrée en cours de mois) ;'
•   calcul du prorata du plafond en cas d'entrée en cours de mois ;'
•   
•   base horaire ;
•   qualification ;
•   catégorie de cotisant ;
•   mutuelle, prévoyance et retraite supplémentaire ;
•   RTT.


Il est donc essentiel ici aussi de vérifier les éléments suivants :
•   calcul du prorata des éléments suivants en cas de sortie en cours de mois : salaire de base, heures supplémentaires mensualisées, indemnités ;
•   présence sur le bulletin des indemnités compensatrices de congés payés et de RTT, le cas échéant ;
•   prorata du treizième mois ;
•   s'assurer que les compteurs de congés payés et de RTT soient vides sur le bulletin puisque les jours acquis par le salarié ont soit été déjà utilisés, soit été payés sur le bulletin en question par le biais des indemnités compensatrices ;
•   indemnités de fin de contrat : ici, il faut faire attention à ce que le libellé de la rubrique utilisée soit cohérent avec le motif de rupture invoqué, que le calcul soit correct et saisi comme il faut sur le bulletin. Par exemple, en cas de rupture conventionnelle, vérifier que le forfait social 20 % se soit bien déclenché ;
•   dans le cas des indemnités de fin de contrat, il faut également vérifier que les seuils d'exonération correspondent à ce qui a été calculé, et que le montant total de ces indemnités soit correct ;
•   en cas de fin de CDD, s'assurer de la présence de l'indemnité de fin de contrat de CDD ;
•   enfin, toujours vérifier le calcul des cotisations et surtout les assiettes, notamment en cas de prorata ou de réintégration sociale.


Suite à la (trop) grande demande de recruteurs par rapport à mon post précédent...

Je tenais à clarifier avec vous quelque chose :

non je ne recherche pas de cdi ou de nouvelles opportunités professionnelles mais merci c'est gentil de proposer.'

VOIR Initialisation des congés payés et des cumuls antérieurs SUR ODOO V8 ET V14
Reprise compteur des congés payés et des provisions de congés payés     X
Initialisation des compteurs        
Congés supplémentaires si applicable


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
GTA

Partie 1 - Maîtrisez les congés payés en France

Les règles d'acquisition des congés payés'
Le principe est le suivant : TOUS les salariés ont droit à des congés payés.

Les stagiaires n'acquièrent pas de congés payés, contrairement aux apprentis et aux contrats de professionnalisation.'

Concernant les salariés à temps partiel, j'insiste très fortement sur le fait que l'acquisition de congés payés est exactement la même que pour les salariés à temps plein.

Selon l'article L 3141-3 du Code du travail, l'acquisition des jours de congés payés se fait au mois le mois de la manière suivante :

2,08 jours ouvrés par mois de travail effectif chez le même employeur ;

2,5 jours ouvrables par mois de travail effectif chez le même employeur.


Lorsque le nombre de jours de congés payés acquis n'est pas un nombre entier, '
il est automatiquement 'arrondi au nombre entier supérieur à la fin de la période de référence'. 
Vous pouvez vous référer à l'article L 3141-7 du Code du travail sur ce point.'

Exemple 1 :

Au bout de 12 mois de travail effectif chez le même employeur, du 1er juin au 31 mai de l'année suivante, '
un salarié acquiert '12 * 2,08 jours ouvrés de congés payés, soit un total de 24,96 jours ouvrés annuels de congés payés. '

Ce nombre est automatiquement arrondi au nombre entier supérieur, soit 25 jours ouvrés annuels de congés payés.

12 * 2,08 = 24,96 => 25

Exemple 2 :

Un salarié travaille un mois entier dans le cadre d'un CDD chez le même employeur. Il acquiert donc 2,08 jours ouvrés de congés payés.'

À la fin du mois et donc de son contrat, ce nombre sera automatiquement arrondi à l'entier supérieur, soit 3 jours de congés payés.'

2,08 * 1 = 2,08  =>  3 

'Les jours supplémentaires de congés payés selon les conventions collectives  '

En d'autres termes, les salariés relevant de cette convention collective, et respectant les conditions d'ancienneté ci-dessus, 
acquerront non plus 25 jours ouvrés de congés payés mais 26, 27, 28 ou 29 jours ouvrés en fonction de leur ancienneté. 

=> soit = 26, 27, 28 ou 29 jours ouvrés en fonction de leur ancienneté

"""""
Les jours supplémentaires de congés payés pour les parents
"""""

controle = 30 avril de l'année précédente' + disposant de 12 jours de congé.

soit = if > 21 ans and == enfants à charge:
if enfants à charge < 15 ans or enfants à charge == handicapé 
result += 2 * enfants à charge <= 30 j ouvrables


controle = 30 avril de l'année en cours' + disposant de 12 jours de congé.

soit = if < 21 :

result = 30 j ouvrables


Exemple :

Si vous ne disposez que de 12 jours de congés payés, vous pouvez tout de même prendre 30 jours de congé. 
Les jours pris au-delà de ses 12 jours de congés ne seront alors pas indemnisés.

Tout salarié de moins de 21 ans au 30 avril de l'année précédente bénéficie de 2 jours de congés supplémentaires par enfant à charge. '
Si le congé acquis ne dépasse pas 6 jours, le congé supplémentaire est réduit à 1 jour.

"""
La période de référence pour l'acquisition des congés payés
"""
La période de référence va du '1er juin au 31 mai' de l'année suivante.'

'Les arrêts de travail'
Si le salarié est absent pendant la période de référence pour l'acquisition des congés payés, '
cela pourra avoir une incidence sur l'acquisition des congés payés elle-même'


'Les règles de prise des congés payés'

Dans un premier temps, il faut préciser qu'il existe en France une période pour la prise des congés payés.'

La période dite des "congés payés" : celle-ci court du '1er mai au 31 octobre'. Elle peut toutefois être étendue à 'toute l'année.''

La période de prise de la cinquième semaine : celle-ci court du '1er mai au 30 avril.'

'Le décompte des congés payés'

Ainsi, le principe est de décompter les jours de congés en 'jours ouvrables', sauf disposition conventionnelle contraire.

Le décompte est le même pour un salarié à temps partiel.

Que se passe-t-il quand un salarié ne prend pas ses congés payés ?

Une fois acquis, les jours de congés doivent être pris.


Si les congés payés n'ont pas été pris en raison d'une :

absence pour congé de maternité ou d'adoption ;'

absence pour accident du travail ou maladie professionnelle ;

absence maladie,

alors les jours de congés sont reportés, même si la période de prise de ces jours est dépassée.

'Les jours de fractionnement'

Dans l'éventualité où le salarié n'aurait pas pris l'intégralité de son congé principal durant cette période, '
et selon le nombre de jours de congés payés qui lui resteraient après le 31 octobre, 
le salarié aurait droit à des jours de congés supplémentaires, qu'on appelle "jours de fractionnement".'

Mais attention : pour pouvoir prétendre aux jours de fractionnement, 
le salarié doit avoir pris au moins 12 jours ouvrables de congés payés consécutifs sur la période principale, soit deux semaines de congés payés à la suite.

Le salarié concerné se verrait dont attribuer :

1 jour de fractionnement s'il lui reste entre 3 et 5 jours de congés à prendre sur son congé principal, mais en dehors de la période principale ;'Période du 1er mai au 31 octobre

2 jours de fractionnement s'il lui reste au moins 6 jours de congés sur la période principale en plus de la cinquième semaine de congés.' Période du 1er novembre au 30 avril


Présentation des règles de calcul de l'indemnité de congés payés (ICP) en France'

Les règles du calcul du dixième:

Le salaire de référence peut être défini comme l'ensemble des salaires du 1er juin au 31 mai, exception faite d'éléments à exclure (présents dans le tableau plus bas).

Il s'agit d'un montant correspondant à priori au 1/10e de la rémunération totale brute perçue pendant la période d'acquisition des congés payés, '
c'est-à-dire généralement du 1er juin au 31 mai de l'année suivante, comme nous avons pu le voir au chapitre précédent.

Les éléments de salaire à intégrer dans la base de calcul doivent tout d’abord présenter un caractère obligatoire pour l’employeur.

Exemple :

Une prime exceptionnelle et facultative ne sera pas prise en compte dans le calcul du salaire de référence.

Les éléments de salaire doivent également représenter la contrepartie du travail du salarié. 

Exemple :

Une prime d'ancienneté, d'objectif, ou une commission seront intégrées dans le calcul du salaire de référence à partir du moment où elles sont attribuées en fonction des résultats personnels du salarié.

Ici, il faut mentionner le fait que la façon dont la prime est versée peut déboucher sur deux règles totalement différentes concernant le calcul du salaire de référence.


En effet, si nous prenons pour exemple la prime d'ancienneté, nous pouvons noter :'

que si la prime est versée en contrepartie du travail, elle doit être intégrée dans le salaire de référence pour le calcul de l'ICP ;'

que si la prime d'ancienneté est versée pendant la période de travail et la période de congés payés, alors il ne faut pas l'inclure dans le salaire de référence. 
Cela reviendrait, comme déjà expliqué, à la payer deux fois. 

'Les absences'

Cet impact dépend du principe d'assimilation de l'absence à du travail effectif.
Ainsi, si l'absence est assimilée à du travail effectif, alors elle doit être intégrée dans le salaire de référence pour le calcul des congés payés.'

'Les règles de calcul du maintien de salaire'


Prenons un exemple où l’horaire est de 7 heures par jour.

Au cours d’un mois de 21 jours ouvrés (soit 21 × 7 = 147 heures), un salarié est en congé 7 jours ouvrés (soit 7 ☓ 7 = 49 heures).

Si le salaire à maintenir est de 2 000 €, la ventilation entre l’indemnité de congés payés (ICP), calculée selon le maintien du salaire, et la rémunération du travail, s’opère comme suit :

indemnité de congés payés = (2 000 × 49) / 147 = 666,67 € ;

rémunération du travail = (2 000 × 98) / 147 = 1  333,33 €.

Mais de nombreuses entreprises recourent à l’une des méthodes forfaitaires simplifiées suivantes pour calculer l’indemnité de congés payés :

Calcul en nombre moyen de jours ouvrables (26) : ICP = (nombre de jours ouvrables de congé × salaire mensuel de référence)/26.

Calcul en nombre moyen de jours ouvrés (21,67, souvent arrondis à 22 pour les horaires répartis sur 5 jours) : ICP = (nombre de jours ouvrés de congé × salaire mensuel de référence)/22.

Calcul en nombre réel de jours ouvrés du mois de prise des congés : ICP = (nombre de jours ouvrés de congé × salaire mensuel de référence)/nombre de jours ouvrés du mois ou payés comme tels.

Calcul en nombre réel de jours ouvrables du mois de prise des congés : ICP = (nombre de jours ouvrables de congé × salaire mensuel de référence)/nombre de jours ouvrables du mois ou payés comme tels.


Je vous propose donc de garder en tête une méthode forfaitaire très souvent utilisée, à savoir le calcul en nombre moyen de jours ouvrés 
: salaire mensuel de référence / 21, 67 x nombre de jours ouvrés de congés payés pris.

'Comparaison entre la règle du dixième et la règle du maintien du salaire'
Le législateur ne s'étant pas prononcé sur ce point, il existe deux méthodes de comparaison.'

La comparaison annuelle : l’employeur maintient le salaire jusqu’à ce que le salarié solde son congé annuel avec la prise de la cinquième semaine, ou bien en fin de période de congé annuel. 
C'est à ce moment-là que la comparaison sera faite entre les deux méthodes de calcul ; et si le calcul du dixième est plus favorable, un complément d’indemnité de congés payés sera versé au salarié.'

La comparaison systématique : l’employeur procède au double calcul à chaque prise de congé et applique la solution la plus avantageuse à chaque fois.

'Cas particuliers:'

Le mode de calcul de l’indemnité légale de congés payés s’applique :

aux congés supplémentaires d’origine conventionnelle ;

aux congés supplémentaires d'origine légale : par exemple les jours supplémentaires pour fractionnement des congés payés.'

Dans le cas du maintien de salaire, le montant journalier de l’indemnité doit simplement être multiplié par le nombre de jours de congé acquis.

Pour le calcul du dixième, il doit être multiplié par le nombre de jours de congé acquis et divisé par le nombre légal de jours acquis au sein de l'entreprise.'

Exemple :

Le dixième de la rémunération est de 2 744 €, soit le montant correspondant à 30 jours ouvrables de congés.

Le salarié ayant droit à 32 jours de congé en application d’un accord collectif, l’indemnité de congés pour 32 jours est de : 2 744 × 32 / 30 = 2  926,93 €.

Impact sur le bulletin de paie
L'article R 3243-1 al 12 du Code du travail précise qu'il y a des mentions obligatoires concernant les congés payés et leur traitement sur le bulletin de salaire.

Ainsi, les informations suivantes doivent obligatoirement apparaître sur le bulletin :

les dates de congés payés ;

le montant de l’indemnité de congés.

'L’indemnité de congés payés a la nature d’un salaire, et est donc :'

soumise à toutes les cotisations et contributions en vigueur ;

soumise à l’impôt sur le revenu


L'indemnité compensatrice des congés payés (ICCP)'

On parle d'indemnité compensatrice de congés payés lorsque les salariés n'ont pas pris les jours de congés payés qu'ils avaient acquis. '


Les situations pouvant donner lieu à une indemnité compensatrice de congés payés
Il s'agit des situations suivantes :'

Rupture du contrat de travail (qu'elle soit causée par l'employeur ou le salarié).

Report des congés payés.

Décès du salarié.


Depuis le 4 mars 2016, l’indemnité compensatrice de congés payés est également due en cas de licenciement pour faute lourde.

Si l’impossibilité de prise des congés payés n’est pas imputable à l’employeur, l’indemnité compensatrice n’est pas due.

Comment doit-on calculer l'indemnité compensatrice de congés payés ?'

L’indemnité compensatrice de congés payés se calcule de la même façon que l’indemnité de congés payés, 
c’est-à-dire maintien de salaire ou dixième de la rémunération annuelle, selon la méthode la plus favorable au salarié.


Chaque indemnité doit être calculée selon la méthode de calcul la plus favorable au salarié.

L’indemnité compensatrice afférente à la période de référence écoulée est exclue de la base de calcul de l’indemnité liée à la période de référence en cours. 

'Les salariés en CDD'

Les salariés en CDD ont droit à une indemnité compensatrice de congés payés pour les jours qui leur restent, quelle que soit la durée de leur contrat.


Il est nécessaire d’inclure le montant de l’indemnité de fin de CDD (prime de précarité) pour le calcul de l’ICCP.

Elle se calcule comme pour les salariés en CDI, mais il faut tout de même préciser les points suivants :

l’indemnité doit être calculée selon les deux méthodes de calcul du maintien de salaire et du dixième, et le montant le plus favorable doit être appliqué ;

l’indemnité de fin de contrat est prise en compte dans la base de calcul de l’ICCP ;

en cas de rupture anticipée du CDD, la rémunération due jusqu’au terme du contrat à titre de dommages et intérêts est exclue de la base de calcul de l’indemnité.

'Calcul sur le bulletin de paie'
L’indemnité compensatrice de congés payés a le caractère de salaire et figure sur le bulletin de paie.

Elle est donc :

soumise à toutes les cotisations et contributions en vigueur ;

soumise à l’impôt sur le revenu.


'En résumé'
Les congés payés sont indemnisés par l'ICP lors de la prise, et par l ICCP lors du départ du salarié des effectifs de l'entreprise.

Deux calculs doivent être systématiquement appliqués : le 'maintien de salaire d'un côté, et le 'calcul du dixième' de l autre côté.

Le plus favorable de ces calculs est celui qui sera versé au salarié.

On utilise ce qu'on appelle le salaire de référence comme base de calcul du dixième.'

Dans le chapitre suivant, nous verrons comment appliquer les calculs des congés payés à des cas concrets.


Appliquez les calculs des congés payés à des cas concrets

"""
'Cas pratiques de l'ICP
"""

'Un salarié est en congé pendant 13 jours ouvrés, du 3 au 19 février 2020.'

'Son salaire de base est de 1 800 € et son salaire de référence de 27 440 €.'

=> Voir fichier Excel ICP ICCP

Question 1
En quelle année les congés payés sont-ils apparus en France ? 

1936
Les congés payés ont vu le jour en France en 1936 suite aux accords de Matignon. À cette époque, les salariés avaient droit à quinze jours de congés payés.

Question 2
Vrai ou faux ? Les cadres dirigeants n'ont pas de droit à congés payés, en application de leur statut.'
Faux
Le principe est que TOUS les salariés ont droit à des congés payés.

Question 3
Que se passe-t-il quand le nombre de jours de congés payés acquis n'est pas entier ?'

Le nombre est automatiquement arrondi à l'entier supérieur'
Si le salarié a acquis à la fin de la période un nombre non entier de jours de congés payés, alors le nombre est automatiquement arrondi à l'entier supérieur. '

Question 4
Quelle est la période de prise de congés payés fixée par la loi ?

Du 1er mai au 31 octobre

Par défaut, la loi a fixé en France les périodes de prise de congés payés suivantes : du 1er mai au 31 octobre pour les "congés payés", 
et du 1er mai au 30 avril pour la cinquième semaine. 

Question 5
Quel élément ci-dessous ne peut être à l'origine de l'acquisition de jours de congés payés supplémentaires ?


L'âge'

L'ancienneté'

# Le poste occupé

Le handicap 
L'article L 3141-10 du Code du travail spécifie qu'il peut arriver qu'une convention, un accord d'entreprise ou d'établissement accordent des congés payés supplémentaires, en raison de l'âge, de l'ancienneté ou du handicap.'

Question 6
Vrai ou faux ? La loi stipule que le salarié en congés payés a droit à une indemnité de congés payés.

Vrai 

L'article L 3141-24 du Code du travail stipule que le salarié en congés payés a droit à une indemnité de congés payés qui lui permet de ne pas perdre son salaire pendant la durée de ses congés.'

Question 7
L'indemnité de congés payés est calculée en fonction :'

Attention, plusieurs réponses sont possibles.

du calcul du maintien de salaire

du calcul du dixième

L'article L 3141-24 du Code du travail précise qu'il existe deux règles de calcul applicables à l'indemnité de congés : le maintien de salaire et le calcul du dixième.'

Question 8
Quels éléments ci-dessous sont intégrés dans le calcul du salaire de référence, pour le calcul du dixième ?

Attention, plusieurs réponses sont possibles.

Les commissions

# Les frais professionnels

# L'indemnité compensatrice de congés payés

Les primes de sujétion

Le principe est de prendre en compte le salaire de base et les éléments de rémunération qui vont venir le compléter, 
à partir du moment où ils viennent rémunérer une période travaillée par le salarié. Cela exclut donc à priori les avantages accessoires et éventuelles prestations en nature, 
dont le salarié ne profiterait pas pendant son congé.

Question 9
Vrai ou faux ? L'indemnité compensatrice de congés payés n'est pas due en cas de report des congés payés.

Faux

Les situations pouvant donner lieu à une indemnité compensatrice de congés payés sont : la rupture du contrat de travail, le report des congés payés et le décès du salarié.

Question 10
Quelle méthode de calcul ci-dessous s'applique quand le salarié acquiert des jours supplémentaires de congés payés ?'


Salaire de référence / 10 / 25 x nombre total de jours acquis x nombre de jours de congés payés pris

# Salaire de base / 10 / 25 x nombre total de jours acquis x nombre de jours de congés payés pris
Salaire de référence / 10 / 25 x nombre de jours de congés pris

"""
Identifiez les règles du maintien de salaire et de la subrogation en cas de maladie
"""
https://www.legisocial.fr/outils-gestion-rh-et-paie/logiciel-gestion-calcul-absences.html

Dans ce chapitre, nous nous pencherons notamment sur les notions suivantes :

'Le maintien de salaire.'

'La subrogation.'

Les règles générales de l'absence maladie'

La Cour de cassation 

Méthode horaire (selon la méthode au mois) : (salaire de base x heures d’absence réelles) / heures réelles du mois.

Méthode du réel (selon la méthode au mois) : (salaire de base x heures d’absence réelles) / heures moyennes du mois.


Pour un salaire à 35 h/semaine, les heures moyennes sont de 151,67 h en raison de la mensualisation.
Cette méthode est celle qu'il faut appliquer lorsque l'absence maladie ne peut pas faire l'objet d'une indemnisation.
La formule de calcul est donc la suivante : 

(salaire brut / nombre d'heures du mois) x nombre d'heures d'absence.'

Cela signifie que si l'absence maladie fait l'objet d'une indemnisation, il reste possible d'utiliser la méthode se basant sur les jours calendaires, 
qui est la même que celle utilisée pour le calcul des 'IJSS'.

La formule de calcul est donc la suivante : 

(salaire brut / nombre de jours calendaires du mois) x nombre de jours calendaires d'absence.'

Exemple :

Un salarié est absent du 14 au 20 mai 2018 pour maladie.

Ce salarié travaille 7 h par jour.

Il est rémunéré 3 000 €. Le mois de mai compte 20 jours de travail, soit 20 * 7 = 140 heures.

Calcul de l'absence en « heures réelles » : (3 000 € / 140 heures) x 35 heures = 750 €.'

Calcul de l'absence en « jours calendaires » : (3 000 € / 30 jours) x 7 jours = 700 €.'


Quels sont les aspects à systématiquement vérifier en cas d'absence maladie d'un salarié ?


Vérifier s'il y a déjà eu des arrêts de travail sur les périodes précédentes : '

nous le verrons plus loin, si certaines conditions sont remplies, la maladie peut être indemnisée par l'employeur, via un maintien de salaire légal ou conventionnel. '
Cette indemnisation obéit à certaines règles en matière de délai. 
Il faut donc être en mesure de dire le nombre exact de jours de maladie du salarié, afin d'évaluer son droit à indemnisation.'

Vérifier l'ancienneté et le statut du salarié : '
cela permettra tout simplement de connaître exactement son droit à indemnisation. 

Vérifier l'application ou non d'une convention collective : 

des conventions collectives peuvent être plus favorables. Dans ce cas, il faudra bien sûr les appliquer.



Quelques précisions

Depuis le 1er janvier 2018, si l'absence du salarié n'est pas indemnisée, alors le plafond du bulletin devra être réduit proportionnellement à la durée de l'absence non rémunérée.'

L’absence pour maladie impacte les calculs suivants :

les congés payés ;

diminution des jours de RTT, pour un mécanisme de RTT reposant sur une logique d’acquisition ;

réduction des primes annuelles calculées sur le temps de travail effectif ;

non-paiement des remboursements de frais professionnels ;

non-attribution de titres-restaurant ;

le cas échéant, impact sur la prime d’intéressement ou la participation aux résultats, si la durée de présence au cours de l’exercice fait partie des critères de répartition, 
ou en raison de la diminution de la rémunération en cas de répartition proportionnelle aux salaires.



Et que se passe-t-il en cas de reprise anticipée du travail ?

Si l'employeur applique la subrogation, alors il doit informer la caisse d’assurance maladie qui verse les IJSS, sous peine de sanction financière.'

Si l'employeur n'applique pas la subrogation, c'est au salarié qui perçoit les IJSS d'informer la CPAM en cas de reprise anticipée de son travail.

Cette mesure vise à lutter contre le versement indu d’IJSS.


'Le maintien de salaire'

Lorsque certaines conditions sont remplies, le salarié peut bénéficier de ce qu'on appelle un "maintien de salaire".'

Il s'agit tout simplement d'une indemnisation opérée par l'employeur, en application du Code du travail ou bien de dispositions conventionnelles, ou d'un usage interne.

Le maintien de salaire vise à verser au salarié tout ou partie de la déduction correspondant à son absence maladie directement sur le bulletin de salaire, 
en attendant le versement d'indemnités complémentaires de la Sécurité sociale.'


Lorsqu'il y a maintien de salaire, le pourcentage de maintien de salaire varie d'une convention collective à l'autre. '
Aussi, le maintien de salaire peut aussi bien être de 100 % que de 70 %.


'Le délai de carence'

Le délai de carence est un dispositif visant à distinguer le début d'une période d'absence indemnisable et le début de l'indemnisation de cette absence.'

Le délai de carence appliqué sur les indemnités complémentaires de la Sécurité sociale

Le décompte du délai de carence des IJSS auprès de la Sécurité sociale s'effectue en jours calendaires. Il est porté à 3 jours.'

Exemple :

Un salarié travaille le lundi 16 avril au matin, puis se rend chez son médecin qui lui délivre un arrêt de travail dans l'après-midi du 16 avril. '

Le délai de carence étant de trois jours calendaires, la Sécurité sociale va comptabiliser trois jours, du 17 au 19 avril, le 16 ayant été en partie travaillé.

Donc, l'indemnisation par la Sécurité sociale sera calculée à partir du 20 avril.'

Le délai de carence ne s'applique pas pour les arrêts suivants :'

accident du travail ;

accident de trajet  ;

maladie professionnelle ;

congé de maternité ;

congé d'adoption ;'

congé de paternité et d'accueil de l'enfant.


'Le délai de carence appliqué sur le maintien de salaire par l'employeur''

Le décompte du délai de carence du maintien de salaire s'effectue en jours calendaires. Il est porté à 7 jours d'après le Code du travail.

En cas de maintien de salaire par l'employeur, il n'y a pas de délai de carence pour les arrêts de travail suivants :

accident de travail ;

maladie professionnelle.

'Le maintien de salaire légal'

Le Code du travail prévoit également quelques conditions afin que cette disposition s'applique, et que le salarié perçoive bien 90 % ou 2/3 de son salaire brut :'

La Sécurité sociale doit prendre en charge l'arrêt de travail dont il est question.'

Le salarié doit être soigné en France, ou dans l'un des pays membres de l'UE ou de l'EEE.'

Le salarié doit avoir fait constater son incapacité à travailler et envoyé l'arrêt de travail à son employeur dans les 48 heures.'

Le salarié doit avoir au minimum un an d'ancienneté dans l'entreprise.

Le cas échéant, le salarié doit faire l'objet d'une contre-visite médicale patronale.

Exemple : 

1. Un salarié a commencé à travailler le 2 janvier 2017. 

Il est mis en arrêt de travail le 26 décembre 2017. N'ayant pas acquis un an d'ancienneté au 26 décembre, les dispositions légales ne s'appliquent pas '
et son employeur n'est pas tenu de lui maintenir son salaire.'

2. Un salarié a commencé à travailler le 2 janvier 2017.

Il est mis en arrêt de travail le 3 janvier 2018. Il a acquis un an d'ancienneté la veille et peut donc faire l'objet d'un maintien de salaire par son employeur, '
en application des dispositions légales.


Comment calcule-t-on le maintien de salaire d'après les dispositions légales ?'


II. Délai de carence

- Maladie non professionnelle, accident non professionnel et accident de trajet : 7 jours calendaires.

- Maladie professionnelle ou accident du travail : pas de délai de carence.



'Le maintien de salaire conventionnel'

En effet, certaines peuvent ne pas appliquer de délai de carence, et même prévoir un maintien du salaire de 100 % du salaire brut.

En effet, ce maintien de salaire peut être calculé sur la base du salaire net et non du salaire brut, comme c'est le cas dans les dispositions du Code du travail.'

L'idée est de s'assurer que le salarié ne perçoive pas un salaire plus élevé pendant son absence que ce qu'il aurait perçu s'il avait réellement travaillé, 
en neutralisant l'avantage causé par l'exonération de cotisations sociales applicable aux IJSS.

'La subrogation'

Nous avons vu plus haut que l'employeur pouvait maintenir le salaire brut du salarié sur son bulletin, '
en attendant de recevoir les IJSS pour les reverser à son salarié au niveau du bulletin de paie. C'est ce qu'on appelle la « subrogation ».

Il existe deux situations possibles :

L'employeur maintient l'intégralité du salaire brut.

L'employeur maintient une partie seulement du salaire brut.'

Lors de la subrogation, l'employeur verse à son salarié des IJSS nettes qui ne sont pas soumises à cotisations.'

L'employeur maintient l'intégralité du salaire brut

Cela signifie que les IJSS lui seront versées directement, sans qu’il ait à obtenir l’autorisation du salarié.

C'est applicable aux :'

IJSS de maladie ;

IJSS de maternité et assimilées (adoption, paternité) ;

IJSS d’accident du travail ou de maladie professionnelle.


L'employeur maintient une partie seulement du salaire brut'


Dans tous les cas, la mise en œuvre de la subrogation suppose que le salaire maintenu soit au moins égal au montant des IJSS.

Maintien de salaire >= IJSS

La subrogation n’est valable que dans la limite du montant du salaire maintenu par l’employeur : 
il ne peut pas conserver les IJSS si leur montant dépasse celui du salaire qu’il verse au salarié.

Quel est l'impact d'une reprise anticipée du salarié sur la subrogation ?

Nous l'avons vu plus haut, en cas de reprise anticipée, l’employeur qui applique la subrogation doit informer la caisse de Sécurité sociale qui verse les IJSS. '
Il s'agit en général de la CPAM dont dépend le salarié concerné ; faute de quoi, il pourrait faire l'objet de sanctions financières.

Les différents types d'arrêts de travail liés à la maladie ou traités de la même manière'

'Le congé de maternité'


Concernant l'indemnisation, le principe est relativement le même que pour l'absence maladie, à savoir le versement d'indemnités journalières, '
dont le montant est calculé en déterminant le gain journalier de base calculé sur la période de référence, divisé par 91,25.

Le salaire pris en compte ne peut pas dépasser le plafond mensuel de la Sécurité sociale en vigueur lors du dernier jour du mois qui précède l'arrêt '

Très important : la CPAM retire à ce salaire journalier de base un taux forfaitaire de 21 %. 
salaire journalier de référence

'Le congé de paternité et d'accueil de l'enfant'

Ce congé bénéficie lui aussi du versement d'une indemnité par la Sécurité sociale.'

La durée du congé de paternité et d'accueil de l'enfant est fixée à vingt-cinq jours calendaires consécutifs, 
avec 4 jours obligatoires à prendre immédiatement après la naissance de l'enfant.'

Ce congé peut succéder au congé de naissance qui, lui, dure trois jours.

Pour ce qui est de l'indemnisation, le Code du travail ne prévoit pas d'indemnisation par l'employeur, donc de maintien de salaire.'

Concernant l'indemnisation, le principe est relativement le même que pour l'absence maladie, à savoir le versement d'indemnités journalières, '
dont le montant est calculé en déterminant le gain journalier de base calculé sur la période de référence, divisé par 91,25.

Le salaire pris en compte ne peut pas dépasser le plafond mensuel de la Sécurité sociale en vigueur lors du dernier jour du mois qui précède l'arrêt '

Très important : la CPAM retire à ce salaire journalier de base un taux forfaitaire de 21 %.
salaire journalier de référence

L'arrêt de travail pour accident de travail ou maladie professionnelle (AT/MP)'

Dans ce cas, il faut bien faire attention, car le montant de l'indemnisation et les conditions de versement sont différents de ceux prévus pour un arrêt maladie.'

Pour un salarié mensualisé, la CPAM détermine comme pour les autres arrêts un salaire journalier de base. 
Ce salaire est calculé en divisant par 30,42 le montant du salaire brut perçu le mois précédant le début de l'arrêt maladie.'

Les indemnités journalières correspondent à un pourcentage de ce salaire journalier de référence qui varie en fonction de la durée de l'arrêt maladie, '
dans la limite d'un montant appelé gain journalier net (le salaire journalier moins 21 %). Le montant est plafonné et évolue dans le temps :'

pendant les 28 premiers jours suivant l'arrêt de travail, '
l'indemnité journalière est égale à 60 % du salaire journalier de base, avec un montant maximum plafonné à 205,84 € au 1er janvier 2020 ;'

à partir du 29e jour d'arrêt de travail, '
l'indemnité journalière est majorée et portée à 80 % du salaire journalier de base, avec un montant maximum plafonné à 274,46 € au 1er janvier 2020 ;'

au-delà de trois mois d'arrêt de travail, '
l'indemnité journalière peut être revalorisée en cas d'augmentation générale des salaires après l'accident.'

Par exemple, 

pour un salarié ayant perçu 2 000 € bruts le mois précédant son arrêt maladie, 

le gain journalier net du salarié pendant son arrêt est égal à [2 000 - (21 % x 2 000)] / 30,42 = 51,93 €.

Les indemnités journalières sont calculées ainsi :

Pendant les 28 premiers jours d'arrêt, le montant des IJ est de (2 000/30,42) x 60 % = 39,44 €.'

À partir du 29e jour d'arrêt, le montant serait de 52,59 €, soit (2 000/30,42) x 80 %.'

La limite du gain journalier net étant dépassée, le montant versé à partir du 29e jour sera ramené à 51,93 €.

La CSG (6,2 %) et la CRDS (0,50 %) sont ensuite déduites du montant des indemnités journalières dues.


En résumé
L'absence maladie entraîne automatiquement une déduction de salaire.'

L'employeur peut, si certaines conditions sont remplies, verser une indemnité au salarié pour compenser la déduction de son salaire, appelée maintien de salaire.'

La Sécurité sociale compense elle aussi la déduction de salaire, sous certaines conditions, via le versement d'indemnités journalières.'

La Sécurité sociale ne rembourse pas les trois premiers jours de l'absence : on appelle cela le délai de carence.'

Si l'employeur maintient le salaire de son employé et demande à recevoir directement les indemnités journalières de la Sécurité sociale, on appelle cela la subrogation.'

"""
Maîtrisez les IJSS et IJ prévoyance

https://www.service-public.fr/particuliers/vosdroits/N526
"""

Il faut prendre le SMIC en vigueur le dernier jour du mois civil précédant celui de l'interruption de travail.'

Pour calculer le gain journalier de base, on applique donc la formule suivante : total des salaires de la période de référence / 91,25.

L’indemnité journalière se calcule en pourcentage du gain journalier de base.

En résumé
En cas d'absence maladie ou autre absence similaire, la Sécurité sociale verse des indemnités journalières de Sécurité sociale (IJSS).'

Ces IJSS ne sont pas soumises à cotisations sociales ou charges ayant la même assiette.

Elles sont soumises à CSG sur les revenus de remplacement et à CRDS, sans abattement, ainsi qu'à l'impôt sur le revenu.

Elles ne doivent pas être intégrées au salaire net imposable sur le bulletin : la déclaration se fait directement sur la déclaration des revenus annuelle.

Les indemnités journalières de prévoyance peuvent parfois prendre le relais des IJSS, en fonction du contrat passé entre l'employeur et l'organisme.


Répercutez correctement les éléments de la maladie sur le bulletin de salaire

Voir fichier Excel

En résumé
Les IJSS nettes n'apparaissent sur le bulletin de salaire qu'en cas de subrogation, car l'employeur doit alors les reverser au salarié, puisqu'il les a perçues à sa place.

Il faut déduire le montant brut des IJSS, avant déduction de la CSG et de la CRDS.

'Quiz'
Calculer en paie les différents éléments de la maladie

Quel est le calcul retenu par la Cour de cassation en cas d'absence maladie non maintenue ?'

La méthode horaire

Dans un arrêt de la chambre sociale du 11 février 1982, la Cour de cassation s'est prononcée en faveur de la "méthode horaire", en raison de sa "stricte proportionnalité". Cela rejoint la nécessité de toujours appliquer le calcul le plus favorable pour le salarié.'

Question 2
Qu'est-ce que le maintien de salaire ?'

Une indemnisation par l'employeur sur le bulletin de salaire'

Il s'agit d'une indemnisation opérée par l'employeur directement sur le bulletin de salaire.'

Question 3
Vrai ou faux ? Le délai de carence distingue le début de la période d'absence indemnisable et le début de l'indemnisation de l'absence en question.'

Vrai

Le délai de carence est en effet la durée entre le début de la période d'absence indemnisable et le début de l'indemnisation de l'absence en question. '

Question 4
Qu'est-ce que la subrogation?'

Le versement des indemnités journalières directement à l'employeur '
Pour compenser le fait qu'il maintient le salaire de son employé pendant son absence maladie, l'employeur peut faire l'avance au salarié et en percevoir ensuite le montant par la CPAM. '

Question 5
Dans quel but verse-t-on les IJSS ?

Pour compenser la perte de salaire causée par l'incapacité temporaire d'un salarié à exercer son activité en raison de maladie

Les IJSS sont destinées à compenser la perte de salaire résultant de la maladie d'un salarié qui est temporairement incapable d'exercer son activité salariée. 

Question 6
Parmi les propositions ci-dessous, lesquelles représentent le régime social à appliquer aux IJSS ?

Attention, plusieurs réponses sont possibles.



Les IJSS sont soumises à la CSG sur les revenus de remplacement et à la CRDS sans abattement

Les IJSS ne sont pas soumises à cotisations de Sécurité sociale

Les IJSS ne sont pas soumises à cotisations de Sécurité sociale et charges ayant la même assiette, mais elles sont soumises à la CSG sur les revenus de remplacement et à la CRDS sans abattement.

Question 7
Vrai ou faux ? Les IJSS ne sont pas soumises à l'impôt sur le revenu.'
Faux
Les IJSS sont soumises à l'impôt sur le revenu. Le montant des IJSS perçues doit donc apparaître dans la déclaration d'impôt de l'assuré.'

Question 8
Comment peut-on définir les indemnités journalières de prévoyance ?

Ce sont des indemnités versées par un organisme extérieur, avec lequel l'employeur a un contrat'

Ce sont des indemnités versées par l'employeur.'

Question 9
Vrai ou faux ? Les IJSS brutes sont déduites sur le bulletin au niveau du brut.

Vrai 

Question 10
Le montant des IJSS doit-il être intégré au montant du net imposable sur le bulletin de paie ?

Non dans tous les cas

C'est au salarié de déclarer les IJSS versées par la Sécurité sociale lorsqu'il effectue sa déclaration de revenus. Donc, en aucun cas le montant des IJSS ne doit apparaître dans le net imposable du bulletin.

"""
Calculez correctement les jours de RTT

"""


35 heures  -    39 heures  =>  4 J RTT acquise/ semaine
35 heures  -    37 heures  =>  2 J RTT acquise/ semaine

151,67 h par mois. 
160,33 h par mois, 
dont 151,67 h au taux normal 
et 8,67 h au taux majoré des heures supplémentaires.


L’employeur doit donc verser ce qu'on appelle une "indemnité compensatrice de jours de RTT", '
qui comprendra le solde des jours de RTT acquis avant le préavis, et les jours de RTT acquis pendant le préavis.

Exemple :

Un salarié a pris 3 jours de RTT dans le mois. Son salaire de base est de 2 857,67 €.

Le calcul de l'absence et de l'indemnisation est le même, à savoir : 

salaire de base / 21,67 * nombre de jours pris.

Absence = 2 857, 67 € / 21,67 * 3 = 395,62 €.

Indemnité = 2 857, 67 € / 21,67 * 3 = 395,62 €.

Attention, parfois le 21,67 peut être arrondi à 22 en fonction des entreprises ; c'est donc un élément à vérifier avant de finaliser le calcul.'

Les jours de repos des salariés en forfait jours

base horaire en forfait jours = 218 inclut la journée de solidarité

result = 365 -(Les samedis et dimanches +Les congés payés (jours ouvrés) +Les jours fériés qui tombent sur un jour travaillé.)

le nombre de jours de repos pouvant être pris par les salariés en forfait jours.= result - 218

Exemple :

En 2019, il y a eu 9 jours fériés tombant sur un jour travaillé.

Le nombre de jours de repos accordés aux salariés en forfait jours était donc :

365 - 104 (samedis et dimanches de l'année) = 261'

261 - 25 (jours de congés payés en jours ouvrés) = 236

236 - 9 (jours fériés tombant sur un jour travaillé) = 227

227 - 218 = 9

En 2019, le nombre de jours de repos (RTT) accordé à un salarié en forfait jours sera donc de 9.

'En résumé'

Les jours de RTT correspondent à une compensation d’heures travaillées au-delà de 35 heures par semaine.

Les jours de RTT ne peuvent pas être assimilés ni remplacer des jours de congés payés.

Les jours de RTT sont généralement proratisés en cas d'entrée ou de sortie en cours de mois.'

Il n'est pas obligatoire de faire figurer les RTT sur le bulletin, mais cela est très recommandé.'


"""
Maîtrisez les règles des absences non rémunérées
"""
'Le congé sans solde'

Sauf dispositions conventionnelles contraires, 'le congé sans solde n’est ni rémunéré', 'ni assimilé à du temps de travail effectif'. 
'Il ne donne pas droit à congés payés et n’est pas pris en compte dans le calcul de l’ancienneté.'

Traitement sur le bulletin de salaire
Pendant le congé sans solde, la rémunération du salarié n’est pas maintenue. On applique donc le calcul reconnu par la Cour de cassation, soit le "calcul au réel".

Exemple :

La salariée Joli est absente du 5 au 16 mars 2018. Son salaire de base est de 2 600 €.

Il y a 22 jours ouvrés en mars, donc 22 * 7 heures de travail par jour = 154 heures réelles en mars.

La salariée est absente 10 jours ouvrés, donc un total de 10 * 7 = 70 heures.

Pour trouver le montant de la déduction, il faut donc diviser le salaire de base par la totalité des heures travaillées en mars, puis le multiplier par le nombre d'heures d'absence.

Soit : (2 600/154) * 70 = 1 181,82 €

La salariée se verra donc déduire 1 181,82 € de son salaire dans une rubrique intitulée de façon à bien être identifiée comme une rubrique de congé sans solde. 

Comme il s'agit ici d’une absence non rémunérée, le congé sans solde doit apparaître distinctement sur le bulletin de paie dans une rubrique spécifique.'

'Un congé sans solde peut entraîner une réduction du plafond. '


'Les absences non justifiées'

L'employeur ne doit jamais considérer qu’il s’agit d’une démission. En effet, comme nous allons le voir plus loin dans ce cours, '
la démission d’un salarié doit résulter d’un acte clair et non équivoque. Dans ce genre de situation, ce n'est clairement pas le cas.'

L'employeur devra alors prendre en compte les conséquences de cette absence sur la bonne marche de l’entreprise, l’âge du salarié, son ancienneté, et l’existence ou non d’un dossier disciplinaire.'

Si le salarié a envoyé un document justificatif tardivement à son employeur, alors le licenciement n'est pas adapté à la situation. '

Impact sur le bulletin de salaire

Au niveau du calcul utilisé, comme pour le congé sans solde, il s'agira de celui reconnu par la Cour de cassation, à savoir le "calcul au réel".'

Exemple : 

Le salarié Martin est absent du 8 au 12 janvier 2018. Son salaire de base est de 3 500 €.

Il y a 23 jours ouvrés en janvier, donc 23 * 7 heures de travail par jour = 161 heures réelles en janvier.

Le salarié est absent 5 jours ouvrés, donc un total de 5 * 7 = 35 heures.

Pour trouver le montant de la déduction, il faut donc diviser le salaire de base par la totalité des heures travaillées en janvier, puis le multiplier par le nombre d'heures d'absence.

Soit : (3 500/161) * 35 = 760,87 €

Le salarié se verra donc déduire 760,87 € de son salaire, dans une rubrique intitulée de façon à bien être identifiée comme une rubrique d'absence non rémunérée. '



En résumé
Toute absence en paie n'est pas forcément rémunérée.'

Le congé sans solde est une absence autorisée par l'employeur suite à la demande de son salarié.'

Il se traduira sur le bulletin par une rubrique de déduction seule, puisqu'il n'y a pas d'indemnisation.'

La prise d'un congé sans solde peut entraîner une réduction du plafond de la Sécurité sociale sur le bulletin de salaire.'


"""
Répercutez correctement les congés pour événements familiaux
"""

Il y a en France énormément de congés différents qui existent pour les salariés, en raison d'événements impactant leur vie familiale. '
Ces congés ne sont pas soumis à une condition d'ancienneté. Les salariés peuvent donc les prendre dès leur arrivée dans l'entreprise.


'Les congés pour événements familiaux'

Les articles L 3142-1, L 3142-4 et L 3142-5 donnent la liste des congés auxquels les salariés ont droit, à condition de présenter un justificatif :

Mariage du salarié ou Pacs : 4 jours.

Naissance, ou arrivée d’un enfant adopté : 3 jours.

Décès du conjoint, du partenaire lié par un PACS, ou du concubin : 3 jours.

Décès du père, de la mère, d’un beau-parent, d’un frère ou d’une sœur : 3 jours.

Décès d’un enfant : 5 jours.

Mariage d’un enfant : 1 jour.

Annonce de la survenue d’un handicap chez un enfant : 2 jours.


Le nombre de jours indiqué ci-dessus est décompté en 'jours ouvrables'. 

Le congé de naissance ne peut pas être cumulé avec le congé de maternité, mais il peut l'être avec le congé de paternité et d’accueil de l’enfant.'


Ces jours d’absence n’entraînent pas de réduction de la rémunération. Ils sont par ailleurs' assimilés à des jours de travail effectif 'pour le calcul des droits à congés payés, 
et pour les droits à majoration de salaire pour heures supplémentaires.

Exemple :

Le salarié a pris des congés payés du 3 avril au 20 avril 2018. La femme de ce salarié a accouché le 16 avril.

Le salarié ne pourra pas poser de congé de naissance du 17 au 19 avril 2018, puisqu'il est déjà en congés payés.'


'Les congés additionnels liés à la famille'

Congé d'adoption'

Cela concerne tous les salariés, dès lors qu'un enfant adopté arrive chez eux. Ce congé s'articule de la manière suivante : il dure 10 semaines lorsqu'il n'y a qu'un enfant adopté. Ce délai démarre généralement le jour de l'arrivée de l'enfant, mais il peut y avoir sept jours consécutifs pris en amont de l'arrivée de l'enfant.

S'il y a trois enfants ou plus à charge dans le foyer familial avec l'arrivée de l'enfant adopté, alors le congé sera porté à 18 semaines, et 22 semaines en cas d'adoption multiple.

Au niveau de l'indemnisation, le salarié reçoit normalement, s'il remplit les conditions requises, des indemnités journalières relatives à la maternité et l'adoption, de la part de la Sécurité sociale.'

Le droit du travail n'oblige en revanche absolument pas l'employeur à maintenir le salaire en complément des indemnités journalières. Mais les avantages conventionnels prévus pour le congé de maternité s'appliquent.'

'Ce congé est assimilé à du temps de travail effectif.'


Ce congé est également cumulable avec un congé spécifique en vue de l'adoption d'un enfant, et un congé rémunéré de trois jours lors de l'arrivée de l'enfant. 
Ce dernier, vous l'aurez compris, est l'équivalent du congé de naissance.

Au niveau de l'impact sur le bulletin, cela se traduira par une rubrique d'absence sur le bulletin pour la durée du congé, avec une déduction de salaire.

Puis, une fois les IJSS versées au salarié, il faudra les faire apparaître sur le bulletin, comme pour les IJSS versées en cas de congé de maternité.


Congé de naissance


Comme évoqué ci-dessus, un congé similaire est accordé en cas d'adoption.'

Le congé de naissance n'est pas cumulable avec le congé de maternité'


Ce congé est, lui, entièrement rémunéré par l'employeur, et assimilé à du travail effectif.'

Sur le bulletin, cela peut apparaître dans les commentaires en bas de bulletin (car l'impact sur la rémunération du salarié est nul), '
ou bien par deux rubriques, une d'absence et une d'indemnisation.


Congé parental d'éducation'
Ce congé peut être pris par un salarié qui aurait un an d'ancienneté à la date de naissance de son enfant.'

Congé de paternité et d'accueil de l'enfant
Ce congé est accordé sans condition d'ancienneté au père de l'enfant et/ou à la personne vivant maritalement avec la mère (conjoint, PACS, concubin ou autre), 
indépendamment du lien de filiation avec l'enfant.'


Depuis les naissances du 1er juillet 2021, ce congé est de 25 jours calendaires et de 32 en cas de naissance multiple (jumeaux ou triplés, par exemple).


Au niveau de l'indemnisation, c'est la CPAM qui verse au salarié des indemnités journalières pendant toute la durée de son congé.

Comme vu précédemment, l'employeur n'a pas d'obligation de maintenir le salaire, mais il existe des conventions collectives qui le prévoient.'


Congé pour enfant malade
D'après l'article L 1225-61 du Code du travail, tout salarié a le droit de s'absenter trois jours par an si l'enfant dont il a la charge, de moins de 16 ans, 
est victime d'une maladie ou d'un accident constaté par certificat médical.

Si l'enfant a moins d'un an, ou si le salarié a au moins 3 enfants de moins de 16 ans à sa charge, alors le congé est de cinq jours par an.

Légalement, ce congé ne donne pas droit à une rémunération par l'employeur. Par conséquent et comme pour les congés évoqués ci-dessus, '
cela se traduira par une rubrique d'absence, avec une déduction du salaire sur le bulletin du salarié.'

Ce congé n'est pas assimilé à du travail effectif.'

En plus de ces congés détaillés, il en existe également en cas de décès, de mariage ou de PACS, de maladie grave du salarié, de l'annonce d'un handicap chez l'enfant '
ou encore de maladie grave d'un proche ou d'un parent dépendant.


En résumé
La loi prévoit un certain nombre de congés dits "pour événements familiaux".

Ces congés sont limités dans le temps selon les dispositions légales, mais peuvent faire l'objet de dispositions conventionnelles ou d'usages plus favorables.

Ils doivent être indemnisés complètement, afin de ne pas porter préjudice au salarié.

'QUIZ'
Question 1
Quel est le but premier des jours de RTT ?

Compenser les heures travaillées au-delà de 35 heures par semaine

Les jours de RTT viennent compenser les heures travaillées au-delà de 35 heures par semaine, dans la limite d'une durée collective hebdomadaire maximale de 39 heures.'

Question 2
Quelle est la pratique la plus courante en matière d'acquisition des jours de RTT ?'

L'application d'une acquisition 

La pratique la plus courante en matière d'acquisition des RTT est justement une logique d'acquisition, qui repose sur l'idée que les jours de RTT vont venir compenser les heures travaillées au-delà de la durée collective retenue par l'entreprise, répartie au mois le mois sur l'année.'

Question 3
Vrai ou faux ? Les jours de RTT sont similaires à des jours fériés chômés.

Faux
Les jours de RTT ne doivent pas être confondus avec les jours fériés chômés. Si un jour de RTT tombe le même jour qu'un jour férié chômé, alors le salarié peut récupérer le jour férié chômé.'

Question 4
Quel calcul est appliqué pour indemniser la prise de jours de RTT ?

Le maintien de salaire

La rémunération du salarié ne doit pas être affectée par les jours de repos. Elle va donc être indemnisée par le biais d'un maintien de salaire.'

Question 5
Qu'est-ce qu'un congé sans solde ?

Un congé non rémunéré soumis à l'accord de l'employeur pour être pris 

Le congé sans solde est un congé non rémunéré, que tout salarié peut demander et qui nécessite l'accord de l'employeur pour être pris. Il s'agit d'une absence non rémunérée.

Question 6
Quel calcul applique-t-on à l'absence en cas de congé sans solde '

Le calcul au réel

Afin d'appliquer un calcul des plus proportionnels et donc le plus favorable au salarié, la Cour de cassation s'est prononcée en faveur du "calcul au réel" lorsqu'on calcule les absences des salariés, notamment le congé sans solde. Soit le calcul suivant : salaire de base / heures travaillées x nombre d'heures d'absence.'

Question 7
Vrai ou faux ? La prise d'un congé sans solde peut entraîner la réduction du plafond de la Sécurité sociale sur le bulletin.'
Vrai
Question 8

Parmi les congés ci-dessous, lesquels sont des congés pour événements familiaux ?

Attention, plusieurs réponses sont possibles.

Le mariage d'un enfant'   =>  des congés pour événements familiaux

L'annonce de la survenue d'un handicap chez un enfant  =>  des congés pour événements familiaux

#L'adoption d'un enfant  =>  relèvent des congés additionnels liés à la famille

#La maladie d'un enfant  =>  relèvent des congés additionnels liés à la famille

Le mariage d'un enfant ou l'annonce de la survenue d'un handicap chez un enfant sont deux des congés pour événements familiaux '
prévus par la loi aux articles L 3142-1, L 3142-4 et L 3142-5 du Code du travail. Les autres congés relèvent des congés additionnels liés à la famille. 

Question 9
Vrai ou faux ? Les congés pour événements familiaux ne sont pas indemnisés.

Faux
Ces absences n'entraînent pas de réduction de la rémunération du salarié qui les prend.'

"""
Détachement en France de salariés étrangers

"""

D'après l'article L 1261-3 du Code du travail, un salarié est considéré comme détaché, au sens transnational, dès lors que :

Son employeur est régulièrement établi et exerce son activité hors de France.

Il travaille habituellement pour le compte de cet employeur.

Il exécute son travail à la demande de celui-ci, pendant une durée limitée, sur le sol français.


Un salarié qui est détaché et travaille en France en dehors du cadre des règlements européens ou d’une convention internationale de Sécurité sociale doit être affilié.

Afin d’inciter les salariés à accepter un emploi à l’étranger, l’employeur peut mettre en place un système particulier de rémunération, avec notamment le versement de primes ou d’indemnités diverses portant des dénominations variées : primes d’éloignement, de vie chère, indemnité logement, de représentation, etc.

Ces éléments de rémunération sont en général classés sous le terme générique de prime d’expatriation, même en cas de détachement, et sont en principe soumis à cotisations.

L’employeur ne serait pas redevable du versement de transport, puisque le salarié travaillant à l’étranger est à priori hors zone de transport.

Sous réserve des conventions internationales, les salaires de source française servis à des personnes qui ne sont pas fiscalement domiciliées en France sont soumis à une
RAS. Dans ce cas, c’est à l’employeur de procéder au précompte de la retenue à la source, et de la verser auprès du service des impôts.

Cette retenue à la source ne doit pas être confondue avec le PAS mis en place en France à partir de 2019.

Elle continuera à s’appliquer en 2019 et les années ultérieures.

Cela implique entre autres que les salariés concernés ne relèveront pas du prélèvement à la source.

Détachement => assujetti à la RAS et non au PAS

Le seul critère fiscal pertinent pour l’assujettissement à CSG est la notion de domicile fiscal. Elle ne doit pas être confondue avec celle de paiement de l’impôt sur le revenu, 
puisqu’une personne ayant son domicile fiscal à l’étranger peut néanmoins payer l’impôt sur le revenu français.

En résumé
Un salarié étranger peut être "détaché" en France par son employeur.

Le détachement signifie qu'une application renforcée des dispositions légales françaises va s'appliquer au salarié détaché.

Les salariés auront par exemple droit aux congés payés.

Ce salarié bénéficie d'un régime social et fiscal spécifique en France.'

"""
Maîtrisez les règles et calculs en cas de départ du salarié
"""


Le calcul des éléments sur le bulletin de salaire

L'indemnité de licenciement'

Le calcul de l'indemnité de licenciement est donc toujours soumis à une comparaison entre le calcul légal et le calcul conventionnel ou autre.'


"L'indemnité ne peut pas être inférieure aux montants suivants :"

1/4 de mois de salaire par année d'ancienneté pour les 10 premières années ;'

1/3 de mois de salaire par année d'ancienneté à partir de la 11e année."'


"Le salaire à prendre en considération pour le calcul de l'indemnité de licenciement est, selon la formule la plus avantageuse pour le salarié :"

Soit la moyenne mensuelle des douze derniers mois précédant le licenciement, ou lorsque la durée de service du salarié est inférieure à douze mois, la moyenne mensuelle de la rémunération de l'ensemble des mois précédant le licenciement.

Soit le tiers des trois derniers mois. Dans ce cas, toute prime ou gratification de caractère annuel ou exceptionnel, versée au salarié pendant cette période, n'est prise en compte que dans la limite d'un montant calculé à due proportion."


Exemple :

Un salarié a un salaire de référence de 1 500 €. Si son ancienneté est de trois ans et six mois, le calcul de l'indemnité minimale sera le suivant :'

[(1 500 x 1/4) x 3] + [(1 500 x 1/4) x (6/12)] = 1 312,50 €

Si son ancienneté est de 12 ans et 9 mois, le calcul de l'indemnité minimale sera :'

[(1 500 x 1/4) x 10] + [(1 500 x 1/3) x 2] + [(1 500 x 1/3) x (9/12)] = 5 125 € 



'Dispositions de la convention collective Syntec :'

Article 18 : 2 ans d’ancienneté et indemnité réduite d’1/3 en cas de « reclassement » hors de l’entreprise.

Article 19 : un montant d’indemnité égal à 1/3 de mois pour les cadres et de 1/4 de mois pour les ETAM sur 20 ans, puis 0,30 au-delà ; 
un salaire de référence qui contrairement à la loi est sur 12 mois seulement, et exclut les majorations pour heures supplémentaires.


Exemple :

Pour un cadre avec une ancienneté de 12 ans et 7 mois, c’est normalement l’indemnité conventionnelle qui s’appliquerait, car plus favorable.

Soit [(2 000 € / 3) x 12 ans] + [((2 000 € / 3) x 7 mois) /12] =

7 999,99 € + 388,89 €  = 8 388,88 € 

Soit une indemnité de licenciement d’un montant total de 8 388,88 €.

NOta :Le terme Etam est un acronyme qui signifie Employés, Techniciens et Agents de maîtrise enre employé et cadres


Certaines conventions collectives prévoient des modes de calcul différents.

Exemple :

Convention collective Industries pharmaceutiques :

 Article 33 : [...] 

2° La base de calcul de l'indemnité de licenciement est la rémunération effective totale mensuelle gagnée par le salarié licencié, pendant le mois précédant le préavis de licenciement. Cette rémunération ne saurait être inférieure à la moyenne des rémunérations mensuelles des 12 mois précédant le préavis de licenciement.'

Pour le calcul de cette rémunération, entrent en ligne de compte, outre le salaire de base, les majorations relatives à la durée du travail, les avantages en nature, les primes de toute nature, y compris les primes de rendement, les primes à la productivité et la prime d'ancienneté, lorsqu'elle est attribuée au salarié, les participations au chiffre d'affaires ou aux résultats à l'exclusion de celles relatives à l'intéressement, la participation et l'épargne salariale, les gratifications diverses ayant le caractère contractuel ou de fait d'un complément de rémunération annuelle, à l'exclusion des gratifications exceptionnelles.

N'entrent pas en ligne de compte les sommes versées à titre de remboursement de frais, le remboursement des frais de transport dans les conditions visées aux articles L. 3261-1 et suivants du Code du travail, les sommes versées au titre de la monétisation des droits issus du compte épargne-temps et, le cas échéant, les primes d'insalubrité ou de travaux salissants, de danger, de froid ou de pénibilité. [...]



L'indemnité compensatrice de préavis'

Ainsi, l'article L 1234-1 du Code du travail fixe les durées minimales de préavis suivantes, en cas de licenciement :'

en dessous de 6 mois d’ancienneté : la durée est déterminée par la loi, la convention collective, les usages ou encore la profession ;

de 6 mois à moins de 2 ans d’ancienneté, => le préavis est d’un mois ;

à partir de 2 ans d’ancienneté, => le préavis est de 2 mois.



La convention collective, les usages de l’entreprise ou le contrat de travail peuvent prévoir des durées de préavis plus favorables, 
c’est-à-dire plus longues en cas de licenciement. Il est également possible de prévoir des conditions d'ancienneté moins importantes.'

Exemple :

La convention collective Syntec prévoit les durées de préavis suivantes :

Un mois pour un employé.

Deux mois pour un employé ayant deux ans d'ancienneté.'

Deux mois, quelle que soit l'ancienneté, pour les employés ayant un coefficient 400, 450 ou 500.'

Trois mois pour les salariés ayant un statut "cadre".


L’indemnité compensatrice correspond aux salaires et avantages, y compris l’indemnité de congés payés, que le salarié aurait perçus s’il avait accompli son travail.


En pratique, comment cela se traduit-il au niveau du calcul ?

Il faut simplement calculer la rémunération moyenne versée au salarié au cours des 12 mois précédant le mois de la notification de la fin du contrat.


Une fois les éléments de chaque mois recensés, il faut additionner le montant de chaque mois puis en faire la moyenne.

Enfin, il faut ajuster ce montant à la durée du préavis.


Exemple :

Pour un préavis d'une durée de 3 mois. '

Le salaire total des 12 derniers mois est de 34 687 €.

Le calcul est donc le suivant : 34 687 / 12 * 3 = 8 672 €.

Attention, en cas de préavis commençant en milieu de mois, il faudra bien évidemment proratiser le montant de chaque mois. 


Assimilable à du salaire, l'indemnité compensatrice de préavis est donc :'

soumise à cotisations sociales ;

soumise à impôt sur le revenu.



'une indemnité de fin de contrat (dite prime de précarité)'

L'indemnité de fin de contrat est égale au minimum à 10 % de la rémunération brute totale versée durant le contrat.'

En cas de renouvellement du CDD, l'indemnité est versée à l'issue du dernier contrat.

Si le CDD est requalifié en CDI (c'est-à-dire transformé en CDI par le juge), l'indemnité de fin de contrat reste due.


L'indemnité de précarité est :'

soumise à cotisations sociales ;

soumise à impôt sur le revenu.


En résumé
Les différents cas de fin ou de rupture du contrat de travail sont soumis à des règles de procédure et de calcul strictes et spécifiques.

Chaque situation donne lieu à la remise des mêmes documents de fin de contrat : certificat de travail, reçu pour solde de tout compte et attestation Pôle Emploi.

Avant de finaliser le dernier bulletin de salaire, il faut penser à vérifier les dispositions légales, conventionnelles et contractuelles.

Cela permet entre autres de garantir la conformité des calculs, mais aussi d'éviter d'oublier des éléments sur le bulletin en question.





"""
calculez-les-indemnites-de-fin-de-contrat
"""
'Les différents calculs existants'

L'indemnité de licenciement (légale, conventionnelle et contractuelle)'
 il s'agira d'appliquer les règles de calcul légales ou bien conventionnelles, 
 et de verser au salarié le montant le plus favorable entre les deux. 
 Il peut toutefois y avoir des cas dans lesquels une indemnité contractuelle est prévue

Le salaire de référence se calcule par rapport à la date de notification de la rupture du contrat de travail.

Il s’agit du montant le plus élevé entre :

la moyenne des salaires bruts , sur les douze derniers mois précédant la notification du licenciement ;

la moyenne des salaires bruts sur les 3 derniers mois précédant la notification du licenciement.

La rémunération doit être comprise comme le salaire brut comprenant tous les éléments de rémunération, 

à l’exclusion 'des remboursements de frais' ; donc, par exemple :

les avantages en nature ;

les primes et éléments variables ;

les primes annuelles pour leur fraction se rapportant à la période de référence ;

l’indemnité de congés payés versée, si les congés payés ont été pris pendant la période de référence.

L’indemnité compensatrice de congés payés.

L’indemnité compensatrice de préavis.

PASS => soit 3 428 * 12 = 41 136 € en 2020

Les seuils d’exonération

Cela signifie que si le montant de votre indemnité de licenciement est inférieur à 82 272 € (soit 2 fois le PASS) en 2020, 
alors il n’y aura pas de cotisations sociales calculées sur la base de ce montant.

if indemnité de licenciement < 2 PASS:
    result = pas de cotisations sociales

Le plan de sauvegarde (PSE)

Selon les articles L 1233-32 et L 1233-61 du Code du travail, il s’agit d’une 
“procédure de licenciement économique englobant au moins 10 salariés sur 30 jours et nécessitant la mise en œuvre de mesures sociales d’accompagnement ou d’un plan de sauvegarde de l’emploi”.

Dans ce cas, les montants sont exonérés d'impôts, sans limitation de montant.'

Sinon, on applique le régime “hors plan de sauvegarde de l’emploi”, c’est-à-dire en cas de licenciement pour motif économique de moindre importance.


Exonération limitée de l'indemnité de licenciement'
L'indemnité versée en cas de licenciement (hors plan de sauvegarde de l'emploi) est en partie exonérée d'impôt sur le revenu.'

Le montant correspondant à l'indemnité fixée par la loi ou la convention collective est exonéré en totalité.'

Si vous avez reçu un montant supérieur, l'exonération est limitée à l'un des montants suivants :

-2 fois le montant de la rémunération brute que vous avez perçue l'année précédant votre licenciement'
-50 % de l'indemnité de licenciement que vous avez perçue'



Attention  

L'exonération est limitée à un maximum de 246 816 € pour les indemnités perçues en 2022 (263 952 € pour les indemnités versées en 2023).'

Exemple :

Un salarié perçoit une indemnité de licenciement de 120 000 € 
dont 70 000 € correspondent à l'indemnité prévue par la convention collective. '
Sa rémunération brute de l'année civile précédant le licenciement est de 40 000 €.'

L'indemnité de licenciement est exonérée à hauteur du montant prévu par la convention collective, soit 70 000 €.'

Ce montant est supérieur à 50 % de l'indemnité perçue (120 000 €/2 = 60 000 €) mais inférieur au double de la rémunération brute annuelle, égal à 80 000 € (40 000 € x 2).'

L'indemnité est donc exonérée à hauteur de la somme de 80 000 €.'

Le surplus de 40 000 (120 000 € - 80 000 €) est imposable.

###=>>>> Dévloppé par DAH on applique le régime “hors plan de sauvegarde de l’emploi”

a=cumul_BRUT N-1   => La rémunération brute N-1 de l'année civile précédant le licenciement'
b=indemnité de licenciement totale perçue
c=indemnité minimale légale ou conventionnelle
d= b/2        =>50 % de l'indemnité totale perçue'
e= 2 * a =>   deux fois la rémunération annuelle brute de l'année civile précédente'

le plus élevé des trois comme seuil d'exonération d'impôt sur le revenu

g = Limite d'exonération'      #=>  le plus élevé des trois comme seuil d'exonération d'impôt sur le revenu
    
result =max(c,d,e)

f=SP * 12 * 6 => 6 PMSS cumulés  

#=> 1)La partie exonérée d’impôt sur le revenu Mais ce montant ne peut pas dépasser 6 PASS

A = result = min(g,f)

# Le surplus de 40 000 (120 000 € - 80 000 €) est imposable à IR
result = b-A  # est imposable à IR

#=> 2)La limite de plafonnement de l’exonération de cotisations, soit 2 PASS (depuis le 1er janvier 2013). En 2020, ce montant est donc de 82 272 €.
h=SP * 12 * 2 => 2 PMSS cumulés  

k = Limite d'exonération'      #=>  Cette limite correspond au plus petit montant entre comme seuil d'exonération de cotisations sociales
 
result = min(A,h)
#Le surplus de 40 000 (120 000 € - 80 000 €) est soumise à cotisation
result = b-k  # est est soumise à cotisation

l = Limite d'exonération'      #=>  Cette limite correspond au plus petit montant entre comme seuil d'exonération  de CSG-CRDS 

result = min(c,k)

#Le surplus de  (120 000 € - 70 000 €) est soumise à  CSG-CRDS
result = b-l  # est est soumise à CSG-CRDS


Si une partie de l’indemnité de rupture du contrat est exonérée d’impôt sur le revenu, alors elle est exonérée de cotisations sociales, MAIS dans une certaine limite.

Cette limite correspond au plus petit montant entre :

1)La partie exonérée d’impôt sur le revenu : 
pour connaître cette limite:
il faut comparer:

1-le minimum légal ou conventionnel de l’indemnité de licenciement ;
2-50 % du montant de l’indemnité totale perçue versée au salarié ;
3-deux fois la rémunération annuelle brute perçue par le salarié durant l’année civile précédant la rupture, 

et prendre le montant le plus élevé des trois comme seuil d'exonération d'impôt sur le revenu. 
Mais ce montant ne peut pas dépasser 6 PASS, soit 246 816 € en 2020.''

2)La limite de plafonnement de l’exonération de cotisations, soit 2 PASS (depuis le 1er janvier 2013). En 2020, ce montant est donc de 82 272 €.

Et pour finir, le montant de l'indemnité sera exonéré de CSG-CRDS pour le montant le plus bas entre :'

Le montant légal ou conventionnel de l’indemnité de licenciement.

Le montant exonéré de l’assiette des cotisations sociales.

"L'indemnité contractuelle de licenciement"

En revanche, il peut être utile de savoir que ce genre de clause contractuelle correspond à ce qu'on appelle une "clause pénale"'
Au niveau du régime sur le bulletin, il faut tout simplement appliquer les mêmes règles que pour l'indemnité légale ou conventionnelle.'

L'indemnité spéciale de licenciement'


'Le licenciement d’un salarié en CDI pour inaptitude d’origine professionnelle'
###=>>>> Dévloppé par DAH on applique le régime “hors plan de sauvegarde de l’emploi” idem ci-dessus
Si l’inaptitude est justifiée, alors il faudra faire le calcul suivant :

Calculer l'indemnité légale de licenciement et la multiplier par deux.'

Calculer l’indemnité conventionnelle, sans multiplier le montant par deux.

Bien évidemment, il faudra par la suite comparer les deux montants et appliquer le plus favorable au salarié.

Au niveau du régime à appliquer sur le bulletin de salaire, on se situe typiquement dans une situation "hors plan de sauvegarde de l'emploi".


'Le licenciement d’un salarié en CDI pour inaptitude d’origine non professionnelle'
###=>>>> Dévloppé par DAH on applique le régime “hors plan de sauvegarde de l’emploi” idem ci-dessus

Dans ce cas, on ne verse pas d’indemnité compensatrice de préavis au salarié ; mais en revanche, la durée du préavis est intégrée dans le calcul de l’indemnité de licenciement.

Au niveau du régime à appliquer sur le bulletin de salaire, on se situe ici encore dans une situation "hors plan de sauvegarde de l'emploi".

Vous pouvez donc vous référer à la section ci-dessus pour les règles de calcul sur le bulletin de salaire.


L'indemnité de départ volontaire'
On parle ici de situations dans lesquelles un salarié va quitter son entreprise de façon volontaire, ou suite à un accord amiable formalisé avec son employeur. 
Cela arrive par exemple en cas de plan de restructuration lié à des difficultés économiques de l’entreprise.

En revanche, si ce départ est exercé en dehors d’un plan de sauvegarde, alors l’indemnité est imposable en totalité.

Elle est également soumise à cotisations sociales et charges ayant la même assiette, ainsi qu’à la CSG et la CRDS, mais sans abattement d’assiette pour ces deux dernières.


L'indemnité de rupture conventionnelle (individuelle et collective)'
L'indemnité de rupture conventionnelle individuelle'
Ici, il faut d’abord vérifier si le salarié concerné est en droit de bénéficier d’une pension de vieillesse d’un régime de retraite légalement obligatoire. 
Ce droit s’apprécie à la date de rupture effective du contrat de travail (à définir). 
Il s'agit tout simplement de voir si le salarié a atteint au moins l'âge légal de la retraite.

Si oui : on applique une exonération d’impôt.

Sinon : on applique le régime de l’indemnité de départ volontaire à la retraite (voir ci-dessous). 

L’indemnité est alors imposable en totalité, soumise à cotisations sociales et autres charges ayant la même assiette, et à CSG et CRDS (mais sans abattement de l'assiette).'

En principe, le montant de l’indemnité de rupture en cas de rupture conventionnelle individuelle est déterminé par l’employeur et le salarié. 
En revanche, il faut que le montant soit au moins égal au montant de l’indemnité légale de licenciement.

Le salaire de référence est calculé de la même façon que pour l’indemnité légale de licenciement.

Pour les salariés ayant moins de 8 mois d’ancienneté, l’administration a considéré que l’indemnité légale était due en cas de rupture conventionnelle individuelle 
AU PRORATA du nombre de mois de présence dans l’entreprise.


L'indemnité de rupture conventionnelle collective'
Le calcul de l’indemnité est défini dans l’accord collectif. Le montant doit au moins être égal à celui de l’indemnité légale de licenciement.

Le montant de l’indemnité est exonéré d’impôt sur le revenu, sans limitation de montant.

Par conséquent, le montant exonéré d’impôt sur le revenu sera également exonéré de cotisations sociales dans la limite de 2 PASS, soit 82 272 € en 2020.

Et enfin, mais à priori cela reste à clarifier, l'indemnité devrait être exonérée de CSG et de CRDS '
dans la limite du montant de l'indemnité légale ou conventionnelle de licenciement, '
ou bien dans la limite du montant exonéré de cotisations sociales (on prend toujours le montant le plus bas entre les deux).

À priori, on n'applique pas de forfait social sur le montant de l'indemnité de rupture conventionnelle collective, 
mais les sources qui se sont prononcées sur ce point n'ont aucune valeur juridique, à savoir l'Urssaf et la DGEFP ; 
donc on attend toujours une clarification juridique expresse sur ce point.


L'indemnité de mise à la retraite'

###=>>>> Dévloppé par DAH on applique le régime “hors plan de sauvegarde de l’emploi” idem ci-dessus
La bonne nouvelle concernant cette indemnité est que les règles de calcul de l’ancienneté et du salaire de référence sont identiques à celles de l’indemnité de licenciement.

Elle est exonérée d’impôt sur la base du montant le plus élevé entre :

Le minimum légal ou conventionnel de l’indemnité de mise à la retraite.

50 % de la somme versée.

2 fois la rémunération brute annuelle de l’année civile précédant la rupture, limitée à 5 PASS, soit 205 680 € en 2020.



L'indemnité de départ volontaire à la retraite'
Sans grande surprise, il s'agit ici du cas où le salarié prend de lui-même sa retraite.'

L'indemnité légale'
Après 10 ans d’ancienneté : 0,5 mois de salaire.

Après 15 ans d’ancienneté : 1 mois de salaire.

Après 20 ans d’ancienneté : 1,5 mois de salaire.

Après 30 ans d’ancienneté :  2 mois de salaire.

Le salaire est calculé en prenant en compte la moyenne des 12 derniers mois précédant le départ à la retraite, ou celle des 3 derniers mois. 
On retient le montant le plus favorable.


L'indemnité conventionnelle'
Si la convention collective prévoit des dispositions plus favorables, il faut bien évidemment les appliquer.

Depuis le 1er janvier 2010, le montant de l’indemnité en cas de départ volontaire à la retraite est imposable (donc soumis à l'impôt sur le revenu) en totalité.'

Il est également soumis à cotisations sociales et charges ayant la même assiette, ainsi qu’à la CSG et la CRDS, mais sans abattement d’assiette pour ces deux dernières. 
C'est-à-dire que vous prendrez le salaire brut de l'employé concerné, sans déduire 1,75 % comme c'est le cas lorsqu'on calcule la CSG et la CRDS sur un bulletin normal.


L’indemnité de rupture anticipée d’un CDD
Par défaut, la rupture anticipée du CDD n’est pas possible, sauf commun accord de l’employeur et du salarié.

Nous allons nous intéresser ici au cas de la rupture d'un CDD par l'employeur une fois la période d'essai écoulée, en l'absence de :

Faute grave.

Force majeure.

Inaptitude du salarié déclarée par le médecin.

L'employeur qui se retrouve dans cette situation doit donc verser au salarié des dommages et intérêts, en application de l'article L 1243-4 du contrat de travail.

Le montant doit être au moins égal à la rémunération que le salarié aurait perçue s'il avait terminé son contrat.'

Le montant des dommages et intérêts sera considéré comme imposable, 
dans la limite du montant qui aurait été versé au salarié s’il avait fini son contrat. Tout montant supérieur est exonéré d’impôt sur le revenu.

Le montant imposable est assez logiquement soumis à cotisations sociales et à la CSG et la CRDS, encore une fois sans abattement d’assiette.

Le versement des dommages et intérêts n'enlève pas au salarié son droit au versement de son indemnité de fin de contrat.'


En résumé
La notion de plan de sauvegarde de l'emploi est importante pour déterminer le régime des indemnités sur le bulletin de salaire.'

Il y a trois niveaux à déterminer pour les seuils d'exonération : impôt sur le revenu, cotisations sociales et CSG/CRDS.'


"""
GTA
Apprenez à distinguer les différentes rémunérations du temps de travail

"""

'Le contingent annuel d heures supplémentaires'

On peut définir ce contingent par la notion de quantité d'heures supplémentaires pouvant être exécutées par un salarié à l'année au sein de son entreprise.

les heures supplémentaires(HS) effectuées au-delà de ce contingent donnent droit à une contrepartie obligatoire en repos

origine réglementaire : les articles L 3121-39 et D 3121-24 fixent alors le contingent annuel à 220 h par salarié.  

contingent_annuel_maximum==220 
if HS > contingent_annuel_maximum:
    result= une contrepartie obligatoire en repos

Le principe est le suivant :

Toute heure supplémentaire effectuée au-delà de la durée légale du travail, ou bien de sa durée d'équivalence, est à comptabiliser sur ce contingent'

durée_légale_travail==35 or 151,67 
if HS > durée_légale_travail:
    result= HS.append(contingent_annuel_maximum)

'Les heures supplémentaires'

Il s'agit, d'après l'article L3121-28, des heures effectuées au-delà de la durée légale du travail.'

Exemple :

Si un salarié a effectué 8 heures supplémentaires à 125 % puis 4 heures à 150 %, son bulletin de salaire devra montrer :

la rubrique de salaire de base à taux normal ;

une rubrique pour heures supplémentaires majorées à 125 %, avec, en base, 8 heures ;
une rubrique pour heures supplémentaires majorées à 150 %, avec, en base, 4 heures ;
Les heures supplémentaires ouvrent également droit, pour les entreprises de moins de 20 salariés, à ce qu on appelle la 'déduction forfaitaire' patronale(DFP).

if Total nombre id employee= ETP < 20:
    result = HS.append(DFP)

"""
Salaires horaires
"""

Programme Python pour calculer le salaire brut

Le salaire brut est le montant d’argent qu’un employé gagne au cours d’une période donnée avant toute déduction. 
Il existe de nombreuses façons différentes de calculer le salaire brut en fonction de la façon dont un employé est payé. 
Cet article décrit les deux méthodes les plus courantes: 'horaire et salaire.'

'Employé rémunéré à l’heure'
Si un employé est payé à l’heure, il reçoit un montant fixe pour chaque heure de travail. 
Donc, s’il est payé 100 / heure et qu’il travaille 8 heures, 
son salaire brut est de 800 . 
Le salaire brut d’un employé horaire doit être calculé sur une 'base hebdomadaire' en raison d’une 'règle appelée heures supplémentaires, '

if type_contract==employee_horaire:
Heures_hebdomadaire== 35
    result = Heures_hebdomadaire
elif Heures_hebdomadaire_supp==HS
    result = Heures_hebdomadaire + Heures_hebdomadaire_supp 

Il stipule que pour les heures supplémentaires:
un employé doit recevoir une rémunération des heures supplémentaires pour les heures travaillées plus de 35 dans une semaine de travail 
à un taux pas moins plus de 1,5 fois les taux de rémunération réguliers. 

Exemple: 'base hebdomadaire'

Supposons que A travaille comme un employé rémunéré à l’heure et qu’il est payé 100 / heure.
S’il a travaillé 40 heures par semaine, 

il recevra la rémunération des heures supplémentaires pour les heures supplémentaires qu’il a travaillées, 
c’est-à-dire qu’il sera payé 1,5 fois 100  pour 5 heures (40-35).

Heures_hebdomadaire :
result = (35) * 100 = 3500

Heures_hebdomadaire_supp : overtimepay
result = (40-35) * 100 * 1.5 = 750

result = Heures_hebdomadaire + Heures_hebdomadaire_supp => 3500+750 = 4250

if working_hours> 35 :
salaire brut total = (salaire_horaire * 35) + (1.5 * salaire_horaire * (heures_travaillées-35)).

if working_hours <35 :
salaire brut total = salaire_horaire * heures_travaillées.

working_hours = 40 soit plus de 35 heures. => heures_travaillées

salaire brut total = 100 * 35 + (1.5) * 100 * 5 => 4250.

payslip.sal_journalier = BASE/26

rub.montant*payslip.sal_horaire     rub.montant = nombre de heures de la période d'emploi(heures_travaillées)'

Programme:

def weeklyPaid(hours_worked, wage): 
    if hours_worked > 35: 
        return 35 * wage + (hours_worked - 35) * wage * 1.5
    else: 
        return hours_worked * wage 
  
  
hours_worked = 40 => heures_travaillées
wage = 100 => salaire
  
pay = weeklyPaid(hours_worked, wage) 

Les heures majorées doivent être distinguées des heures à taux normal, mais également selon le taux de majoration appliqué.

ex = Maroc

    def get_total_hs125(self):
            record.totalHS125 = total * 125 / float(100) * sal_base / 191

    def get_total_hs150(self):
            record.totalHS150 = total * 150 / float(100) * sal_base / 191

    def get_total_hs200(self):

            record.totalHS200 = total * 150 / float(100) * sal_base / 191



'Les heures complémentaires'

Il s'agit d'heures effectuées par un salarié à temps partiel. 

Elles peuvent être effectuées dans la limite de 1/3 et/ou 1/10e(conventionnelles) de la durée de travail prévue par le contrat de travail.

Si les heures complémentaires atteignent ou dépassent la durée légale de travail, alors le contrat peut être requalifié en contrat à temps plein(ETP).

durée_légale_travail==35 or 151,67 
if HC >= durée_légale_travail:
    result = HC.append(type_contract==employee_horaire==ETP)


'Le paiement des heures complémentaires'
Exemple :

Un salarié travaille 30 heures par semaine. Il peut donc réaliser 3 heures complémentaires en application des dispositions légales.

Si des dispositions conventionnelles le prévoient, il peut réaliser jusqu'à 10 heures complémentaires.'

Si tel était le cas, les 3 premières heures seraient majorées de 10 %, tandis que les 7 heures suivantes le seraient de 25 %. 


Il s'agit d'heures effectuées par un salarié à temps partiel. 

Elles peuvent être effectuées dans la limite de 1/3 et/ou 1/10e(conventionnelles) de la durée de travail prévue par le contrat de travail.

if type_contract==employee_temps_partiel:

HC== dans la limite de 1/3 et/ou 1/10e(conventionnelles)

    result = Heures_hebdomadaire*1/10e *10% + (Heures_hebdomadaire*1/3 - Heures_hebdomadaire*1/10e) * 25% 


'Le calcul du plafond réduit'

Salarié à temps partiel

valeur mensuelle du plafond x (durée contractuelle + heures complémentaires) / durée légale* du travail ou Si la durée conventionnelle est inférieure à la durée légale de travai


Exemple :

Un salarié mensualisé a un contrat à temps partiel de 32 h/semaine (soit 138,67 h/mois) dans une entreprise où la durée collective du travail est de 35 h hebdomadaires (soit 151,67 h/mois).

En 2019, le plafond applicable à sa paie est de :

plafond mensuel × 138,67 h/151,67 h

Si au cours d’un mois il fait 10 heures complémentaires majorées de 10 %, le plafond de cette paie est de :

plafond mensuel × (138,67 h + 10 h)/151,67 h

Les heures complémentaires ne donnent pas droit à la déduction forfaitaire patronale attachée aux heures supplémentaires.

Les heures supplémentaires et complémentaires bénéficient, depuis le 1er janvier 2019, d'une réduction de cotisations sociales et d'une exonération d'impôt sur le revenu.'

La réduction des cotisations sociales porte sur les cotisations d'assurance vieillesse et d'assurance veuvage.

La réduction d'impôt est limitée à 5 000 € par an.'


'Les heures de nuit'
Le travail de nuit est forcément exceptionnel.

Cela signifie entre autres qu'il doit :'

être systématiquement justifié par l'employeur comme nécessaire pour assurer la continuité de l'activité économique ou des services d'utilité sociale ;'

prendre en compte les impératifs de protection de la santé et de la sécurité des travailleurs (article L 3122-1 du Code du travail).


l'article L 3122-20 du Code du travail prévoit que la durée du travail de nuit va de 21 h à 6 h du matin.'

Quelles sont les contreparties possibles au travail de nuit ?
Il en existe deux :

le repos compensateur d'une part, et la compensation salariale d'autre part.

'Les heures de récupération'

La récupération ne peut pas faire augmenter la durée normale du travail de plus d'une heure par jour, ou de huit heures par semaine.'

En revanche, les heures de récupération ne sont pas prises en compte pour le calcul des heures supplémentaires 
puisqu'encore une fois, il s'agit d'heures normales qui ont été déplacées.'


'Le repos compensateur'

'1-La contrepartie obligatoire en repos'

Elle se déclenche en cas d'accomplissement d'heures supplémentaires

contingent_annuel_maximum==220 
if HS > contingent_annuel_maximum:
    result= une contrepartie obligatoire en repos or indemnité_compensatrice en cas(décès ou départ du salarié, les heures de repos acquises n'atteignent pas 7 heures)'

result = indemnité_compensatrice == (le nombre d’heures acquises/la durée normale de la journée de travail dans l’entreprise)

Dans certains cas, la prise de la contrepartie obligatoire en repos peut être remplacée par ce qu'on appelle une indemnité compensatrice :'

décès ou départ du salarié ;

les heures de repos acquises n'atteignent pas 7 heures.'

Dans ce cas, on calcule l'indemnité compensatrice en rapportant le nombre d’heures acquises à la durée normale de la journée de travail dans l’entreprise.'

result =  indemnité_compensatrice == (le nombre d’heures acquises/la durée normale de la journée de travail dans l’entreprise)

'2-Le repos compensateur de remplacement'

Il peut être utilisé à la place de la rémunération d'une partie ou de toutes les heures supplémentaires effectuées par les salariés.'

Au niveau du calcul, le plus simple est d'illustrer le remplacement du paiement des heures supplémentaires par un repos compensateur, via un exemple de calcul.'

durée_légale_travail==35 or 151,67 
if HS > durée_légale_travail:
    result= HS.append(contingent_annuel_maximum)
else:
    result= HS.append(Le repos_compensateur_remplacement)== Transcrit en heures

Exemple :

'Transcrit en heures:'

Dans une entreprise où le paiement des heures supplémentaires est remplacé en totalité par un repos compensateur, 
40 h au cours d’une semaine donneront lieu à 5 h supplémentaires remplacées par un repos compensateur à hauteur de :

125 % pour les heures effectuées entre 35 h et 39 h, donc 4 × 125 % = 500 %

Transcrit en heures, cela donne donc 5 heures de repos.

On y ajoute 125 % pour la 5e heure supplémentaire, soit 1 h et 15 min.

En effet, la transcription des 25 %, 50 %, 75 % se fait selon les quarts d'heure, soit 15 minutes, 30 minutes et 45 minutes.'

result(1) = 125 % *HS(39-35)  =  4 × 125 % = 500 % * 60 = 5 H
result(2) = 125 % *HS(40-39)  =  1 × 125 % = 125 % * 60 = 75 min = 1 h + 15 min
Total = result(1) + result(2) =  6 h + 15 min  de repos

Le repos compensateur de remplacement sera donc de 6 h et 15 min.

'Le principe de l'heure d'astreinte'

"...période pendant laquelle le salarié, sans être sur son lieu de travail et sans être à la disposition permanente et immédiate de l’employeur, "
a l’obligation d’être en mesure d’intervenir pour effectuer un travail au service de l’entreprise" (article 3121-9 du Code du travail)."

L'astreinte peut concerner n'importe quel salarié, mais pas les cadres dirigeants.
Il ne faut pas oublier que depuis la loi Travail, les accords d'entreprise priment sur les accords de branche, même si ces derniers sont plus favorables.'

Il peut y avoir deux formes de contrepartie, mises en place selon les situations par l'accord collectif ou l'employeur :

financière ;

sous forme de repos.

En cas de contrepartie financière, le montant de celle-ci peut être inférieur au SMIC. On considère en effet que l'astreinte n'est pas équivalente à du travail effectif.

En revanche, si les conditions de l'astreinte ne sont pas remplies, autrement dit si le salarié reste à l'entière disposition de son employeur 
sans pouvoir exécuter ses occupations personnelles (par exemple s'il est de permanence au travail), '
alors cela est considéré comme du travail effectif et doit donc respecter le SMIC et/ou le minimum conventionnel pour l'indemnisation financière.'

Comme nous l'avons évoqué, l'astreinte ne constitue pas juridiquement du travail effectif.

Cela signifie entre autres que les périodes d'astreinte sont prises en compte dans le calcul des durées minimales de repos quotidien ou hebdomadaire.'

Ainsi, s'il n'y a pas d'intervention pendant l'astreinte, l'employeur peut considérer que le salarié a pu bénéficier de son repos minimal, quotidien ou hebdomadaire.'

En revanche, s'il y a une intervention et que le salarié n'a pas déjà profité du minimum de repos au début de l'intervention, alors il doit bénéficier, à la fin de l'intervention, 
de l'intégralité de son repos minimal, quotidien ou hebdomadaire.'

Au niveau de la contrepartie financière, elle sera soumise à cotisations sociales et fiscales, au même titre que le salaire de base

'En résumé'
La durée légale du travail est fixée à 35 heures hebdomadaires, en France.

Il est toutefois possible de travailler au-delà de cette limite, moyennant compensation.

Une des compensations possibles est le repos compensateur.

Une autre compensation est le paiement, généralement majoré, des heures travaillées au-delà de la durée légale du travail, ou de la durée contractuelle.


'Répercutez correctement les différentes primes'

Le temps d'habillage et de déshabillage'

En cas d'obligation de porter une certaine tenue dans le cadre du travail, '
l'employeur doit mettre en place des contreparties par rapport au temps nécessaire à l'opération d'habillage et de déshabillage.'

Cela ne vaut que si le salarié est obligé de s'habiller ou se déshabiller sur son lieu de travail.'


'Les primes compensant une réduction du temps de travail'

le fait de réduire le temps de travail collectif de l'entreprise s'est fait par le biais d'accords.'

Ces accords ont, le plus souvent, prévu que cette réduction du temps de travail s'accompagnait d'un maintien du salaire pour les employés.

'La prime d’assiduité'
C'est une prime dont la finalité est d'encourager et de récompenser la présence assidue du salarié au travail.

'Les primes de résultat'
L'exemple le plus classique est la prime de bilan.'

Il s'agit de primes versées au salarié en fonction de ses résultats, ou encore de ceux de l'entreprise en général.

'Les primes de sujétion'
On peut définir les primes de sujétion comme des primes qui compensent une servitude ou un danger inhérent à l’emploi du salarié

'En résumé'
Il existe énormément de primes différentes mises en place afin de compléter le salaire de base.

Ces primes correspondent à un complément de salaire.

Ces primes sont soumises à cotisations.

Ces primes sont imposables.

'Maîtrisez les éléments complémentaires du salaire de base'

'La commission'
Le RF Paye définit cet élément comme un “pourcentage des commandes ou du chiffre d’affaires du salarié”. 
Cela concerne donc essentiellement les salariés travaillant dans la vente.

La commission ne doit pas être confondue avec la prime sur objectif.

'Le rappel de salaire'
Le rappel de salaire est “un élément versé après la période d’emploi à laquelle il se rapporte”.

On peut distinguer les rappels de salaire en trois catégories :

'les rappels de salaire versés pendant la durée d’exécution du contrat de travail'

À partir de 2018
Les taux et plafonds appliqués sont désormais ceux de la période d’activité concernée par le rappel de salaire.

'les rappels de salaire versés après la rupture du contrat de travail ;'

À partir de 2018
On appliquera les taux et plafonds en vigueur lors de sa dernière période d’emploi.

'les rappels de salaire versés suite à une décision de justice.'

les taux et les plafonds de Sécurité sociale applicables à ces montants sont ceux qui correspondent à la période d’activité concernée par le rappel de salaire.

'La prime d’ancienneté'

Il s'agit d'un avantage accordé aux salariés en se fondant sur la durée passée à travailler pour la même entreprise. 
On peut dire que cela vient récompenser la fidélité des salariés au même employeur.

L'origine de cette prime est conventionnelle et non légale. Cela signifie que les règles à appliquer doivent être vérifiées pour chaque employeur, '
en fonction de la convention collective dont il dépend.

Il faut ajouter la prime d'ancienneté au salaire de base prévu dans le contrat, et non l'y intégrer.

La prime d'ancienneté peut se présenter sous différentes formes :'

un montant forfaitaire ;

un pourcentage du salaire de base, du salaire brut total ou encore du minimum conventionnel ;

une gratification occasionnelle non mensualisée.

En cas de travail à temps partiel ou de départ de l'entreprise en cours de mois, la prime d'ancienneté doit être proratisée, 
SAUF s'il s'agit d'un montant forfaitaire.'

'La prime de fin d’année ou de treizième mois'

Il s'agit d'une prime annuelle, donc calculée sur toute l'année de travail et versée généralement en une fois à la fin de la période concernée/en deux fois dans l'année.

Il convient de calculer la prime au prorata temporis du temps de travail effectué pour les salariés à temps partiel, 
SAUF s'il s'agit d'un montant forfaitaire.'

'En résumé'
Certains éléments de rémunération viennent récompenser le travail du salarié, que ce soient les efforts fournis, les résultats, ou encore sur la base du mérite.

Ces éléments sont soumis à cotisations sociales au même titre que le salaire de base. Ils sont également imposables.

'Compétences évaluées'
Maîtriser les éléments variables impactant le brut

Question 1
Quelle est la durée légale du travail en France ?
35 heures
L'article L 3121-7 du Code du travail fixe la durée légale de travail effectif des salariés à temps complet à 35 heures par semaine.'

Question 2
Que sont les heures complémentaires ?

Ce sont des heures effectuées par un salarié à temps partiel au-delà de son horaire contractuel

Les heures complémentaires sont les heures effectuées par un salarié à temps partiel. Ces heures s'ajoutent à l'horaire contractuel du salarié, 
tout en ne dépassant pas la limite légale.

Question 3
Quelles sont les compensations possibles en cas d'heures effectuées au-delà de la durée légale en France ?'

Attention, plusieurs réponses sont possibles.

Compensation salariale
Compensation via repos
Les heures supplémentaires font généralement l'objet d'une compensation salariale, 
via soit une majoration de salaire, soit une compensation par repos, voire les deux, selon les textes applicables.

Question 4
Quelle est la définition des primes de sujétion ?

Des primes de sujétion sont des primes qui compensent une servitude ou un danger inhérent à l’emploi du salarié


Question 5
Parmi les propositions suivantes, lesquelles entrent dans la catégorie des primes de sujétion ?

Attention, plusieurs réponses sont possibles.

La prime de froid

#La prime d'ancienneté

#La prime de résultat

La prime d’insalubrité
La prime de froid et la prime d'insalubrité sont des primes visant à compenser la difficulté des conditions rencontrées par les salariés dans le cadre de l'exécution de leur travail. 
Les primes d'ancienneté et de résultat viennent récompenser la fidélité du salarié, pour la première, et l'efficacité de son travail, pour la deuxième.

Question 6
Quelle est la nature de la prime de résultat ?
Collective

La prime de résultat est une prime à caractère collectif, dans le sens où c'est l'effort de toute l'entreprise qui est analysé. '

Question 7
La prime d'ancienneté peut-elle être proratisée ?'

Oui, sauf en cas de montant forfaitaire

En cas de travail à temps partiel ou de départ de l'entreprise en cours de mois, la prime d'ancienneté doit être proratisée, SAUF s'il s'agit d'un montant forfaitaire.'

Question 8
Comment définir la commission ?

Un pourcentage du chiffre d’affaires du salarié
Le RF Paye définit cet élément comme un “pourcentage des commandes ou du chiffre d’affaires du salarié”. 
Cela concerne donc essentiellement les salariés travaillant dans la vente.

Question 9
Vrai ou faux ? La commission peut constituer le seul moyen de rémunération des salariés.

Vrai

La commission concerne essentiellement les salariés travaillant dans la vente. 
Ils peuvent être rémunérés uniquement par le biais de commissions, ou bien par un salaire de base fixe d'une part, et des commissions d'autre part.

Question 10
Vrai ou faux ? Le rappel de salaire ne peut être versé que pendant la durée d'exécution du contrat du salarié.'
Faux
Le rappel de salaire peut également être versé suite à la rupture du contrat de travail, ou bien suite à une décision prudhommale.

'Maîtrisez les avantages en nature en paie française'

'Les principes encadrant l'avantage en nature

Un avantage en nature est une prestation fournie par l’employeur au salarié, lui évitant ainsi une dépense.

Voici quelques exemples d'avantage en nature :'

véhicule ;

logement ;

NTIC ;

nourriture ;

voyages ;

produits ou services réalisés par l'entreprise ;'

bons d'achat et cadeaux ;'

place de parking ;

compte de dépôt à vue rémunéré ;

prise en charge des contraventions routières.

Quelle est la valeur de l'avantage en nature à retenir ?'
Les avantages en nature peuvent être calculés de différentes façons :

On prend en compte la valeur réelle de l'avantage, que l'employeur doit alors calculer.

On prend en compte la valeur prévue par la convention ou les accords de travail.

Si la valeur prévue par la convention ou les accords de travail est inférieure, alors on prend en compte la valeur prévue par le contrat de travail.


Pour les avantages en nature logement et nourriture, on applique une valeur forfaitaire, 
en cas d'absence de calcul prévu par la convention ou les accords collectifs de travail.'

Pour les salariés apprentis ou titulaires d'un contrat de professionnalisation, on applique seulement 75 % de la valeur de l'avantage en nature sur le bulletin de paie.


'Quel est le traitement sur le bulletin de paie ?'

L’avantage en nature doit obligatoirement figurer sur le bulletin de paie.

en positif au niveau du salaire brut pour être soumis à cotisations ;

en négatif, et pour le même montant, après le net imposable, afin d'être déduit du salaire net à verser au salarié.'

L'avantage en nature doit être pris en compte pour vérifier si le SMIC ou le minimum conventionnel est bien respecté.'


C'est un élément qui est également intégré dans le calcul du salaire de référence pour les congés payés, SAUF SI le salarié continue à bénéficier de cet avantage pendant ses congés.'

Le principe est le suivant : à partir du moment où le salarié conserve l'usage de l'avantage en nature dans sa vie personnelle, 
ce dernier ne peut pas lui être retiré pendant la suspension de son contrat de travail.

La maladie
Comme expliqué au-dessus, si le salarié continue de bénéficier de son avantage pendant sa maladie,
alors l'avantage en nature est maintenu, sauf disposition contractuelle contraire.'

Le préavis
Il est impossible de retirer l'avantage en nature à un salarié pendant la durée d'exécution de son préavis.
Si c'est le cas, alors l'employeur peut être amené à lui verser une indemnité compensatrice.

Quelques exemples d'avantage en nature'

NTIC (nouvelles technologies de l'informatique et de la communication)'

mis à disposition de manière permanente ; autrement dit, de manière à ce que le salarié en ait également une utilisation privée. 

L'avantage en nature est donc constitué par cette utilisation privée.'

L'appréciation se fait alors au réel (selon le coût engagé par l'utilisation de cette technologie) ou au forfait.

Si l'utilisation de ces technologies mises à disposition des salariés par leur employeur est uniquement privée, alors l'appréciation de l'avantage en nature ne se fera qu'au réel.

'Voyages'

On parle ici de voyages d'affaires ne donnant pas lieu à des frais d'entreprise

que l'intérêt de l'entreprise n'était pas prouvé pendant ce voyage d'affaires, et l'ont donc requalifié en avantage en nature soumis à cotisations.'

'Produits ou services réalisés par l'entreprise''

Il s'agit ici de la remise gratuite de produits fabriqués par l'entreprise.

Bons d'achat et cadeaux'

Les cadeaux sont considérés comme un avantage en nature. Le montant pris en compte doit normalement correspondre à la valeur réelle du cadeau.

Il existe cependant des exonérations :

si le cadeau en question est attribué par le CE ou le CSE (comité social économique), pour les entreprises de 50 salariés et plus ;

si le cadeau est attribué par l'employeur en l'absence de CE ou de CSE, pour les entreprises de moins de 50 salariés.

'Place de parking'

Si une place de parking est mise à disposition du salarié de manière permanente, alors cela constitue un avantage en nature.

'Prise en charge des contraventions routières'

Cela concerne les cas où le salarié commet une infraction routière alors qu’il utilise un véhicule immatriculé au nom de l’employeur.

L'avantage en nature véhicule'

Quand un employeur met à la disposition d’un salarié un véhicule dont il est propriétaire ou locataire, de façon permanente, 
alors l’utilisation privée qui en est faite représente un avantage en nature qui doit être soumis à cotisations sociales.

'En pratique, il y a donc avantage en nature dès que le salarié peut utiliser un véhicule professionnel à titre privé, en dehors de son temps de travail.'

L’avantage en nature peut être évalué soit sur la base des dépenses réellement engagées, soit sur la base d’un forfait annuel.

L'avantage en nature logement'

Si l’employeur fournit, gratuitement ou pour un prix modique, un logement au salarié, cela constitue un avantage en nature soumis à cotisations sociales.

La prise en charge par l’employeur du loyer dû par le salarié ne constitue pas un avantage en nature, mais un avantage en argent.

Afin de déterminer le montant de l'avantage en nature logement, autrement dit l'assiette qui sera soumise à cotisations sociales, l'employeur peut :'

procéder à l’évaluation forfaitaire en fonction d’un barème ;

procéder à l’évaluation sur la base de la valeur locative.

L'avantage en nature nourriture'

Il s'agit des situations dans lesquelles le salarié est nourri gratuitement ou pour un prix modique par l’employeur, hors la situation du déplacement professionnel.'

Pour ce qui est de l'évaluation de l'avantage en nature nourriture, on applique un montant de 9,80 € par journée, soit 4,90 € par repas en 2020.

Cela implique notamment que si le salarié est nourri par le biais d'une participation inférieure à la valeur forfaitaire, '
la différence entre cette valeur et la participation du salarié est réintégrée dans l’assiette des cotisations.

'Exemple :'

Un salarié participe à hauteur de 1,50 € par repas.

Les avantages en nature nourriture soumis à cotisations sont de : 4,90 € – 1,50 € = 3,40 €.


'En résumé'
L'avantage en nature est un élément très particulier de la paie française.'

Il impacte le brut en positif, afin que les cotisations sociales soient déduites du montant.

Il est intégré au salaire net imposable.

Il n'est jamais payé au salarié.'

Il doit être déduit avant le salaire net.


'Identifiez les différents frais professionnels'

Principes généraux
L'arrêté du 20 décembre 2002 définit à son article 1 les frais professionnels comme des '
"charges de caractère spécial inhérentes à la fonction ou à l’emploi du salarié, que celui-ci supporte au titre de l’accomplissement de ses fonctions".

Un point de vigilance pour le gestionnaire de paie repose sur la qualification des frais professionnels. 
Ainsi, il apparaît que la frontière entre frais professionnels et avantages en nature peut être difficile à déterminer.

La question de la qualification est particulièrement importante, car cela permet de déterminer si l'élément concerné doit ou non rentrer dans la base de calcul de certaines indemnités.'

Exemples :

l'indemnité de licenciement ;'

l'indemnité de congés payés.'

Les frais professionnels sont régis par un principe très important, 
selon lequel tout frais généré pour les besoins de son activité professionnelle et dans l'intérêt de son employeur doit être remboursé au salarié.'

L'arrêt du 12 décembre 2012 indique notamment que si le contrat précise que les frais doivent être remboursés par le salarié, alors cette clause sera réputée non écrite. '
En d'autres termes, cela signifie qu'elle ne sera pas appliquée. Le reste du contrat de travail, quant à lui, reste valable.

La prescription des frais professionnels est de trois ans, comme pour les salaires.


Voici quelques exemples de frais professionnels :

frais de déplacement ;

frais de restauration sur le lieu de travail ou hors de l'entreprise ;'

mutation, déménagement ;

télétravail ;

nouvelles technologies ;

vêtements.


Les frais professionnels ne doivent pas être confondus avec un autre élément mentionné au début de ce cours, à savoir les frais d'entreprise.'

Ces derniers ne sont ni des avantages en nature, ni des frais professionnels, ni une rémunération.

Leur remboursement est toujours exonéré de cotisations, et doit répondre à des critères bien spécifiques pour être qualifié de frais d'entreprise.'


'Les frais de nourriture'

'Les titres-restaurant'
il faut préciser que les titres-restaurant ne rentrent ni dans la catégorie des frais professionnels, ni dans celle des frais d'entrepris'

L'employeur n'est pas obligé de remettre des titres-restaurant à ses salariés.

La participation patronale est exonérée de cotisations et d'impôt sur le revenu si :'

Le montant est compris entre 50 % et 60 % de la valeur du titre.

Le montant ne dépasse pas une valeur forfaitaire par titre-restaurant : en 2020, cette valeur a été fixée à 5,55 €.

La part du salarié est retenue sur son bulletin de salaire.

Les titres-restaurant peuvent être attribués aux salariés titulaires d'un contrat de travail, y compris les contrats aidés (apprentissage ou professionnalisation, par exemple).'

L'employeur doit également attribuer des titres-restaurant aux stagiaires.'

Le salarié ne doit pas recevoir de titre-restaurant s'il n'y a pas de travail effectif comme par exemple :

arrêt maladie ;

congé de maternité ;

congés payés ;

dispense de préavis ;

jours fériés.

'La prime de panier'

On peut également parler d'allocation forfaitaire versée aux salariés au titre de "frais professionnels". Le but ici est de les indemniser des frais qu'ils sont amenés à engager

En principe, cet élément est exonéré de cotisations et autres contributions au titre des frais professionnels. 
Dans ce cas, le montant exonéré est exclu de tout calcul de paie (comme par exemple la base de calcul des majorations pour heures supplémentaires, ou le salaire de référence des congés payés).

Dans le cas où une partie de la prime de panier serait soumise à cotisations, alors cette part est intégrée dans certains calculs.

Exemple :

vérification du salaire minimum ;

indemnités de congés payés et de rupture, etc.

Afin de bénéficier de l'exonération mentionnée ci-dessus, la prime de panier doit remplir les conditions suivantes :'

le salarié est placé dans des circonstances de fait entraînant des dépenses supplémentaires de nourriture ;

les allocations sont utilisées conformément à leur objet ;

l’employeur n’applique pas de déduction forfaitaire spécifique pour frais professionnels.


Pour déterminer si la prime de panier est bien utilisée selon son objet, un des éléments est de vérifier qu'elle ne dépasse pas les valeurs suivantes :'

6,70 € par repas pour les allocations de restauration sur le lieu de travail ;

9,30 € par repas pour les allocations de restauration hors des locaux de l’entreprise, ou sur un chantier. 


Ces valeurs sont celles de 2020.

Il y a alors deux possibilités :

L'employeur ne justifie pas le dépassement, auquel cas le montant doit être réintégré au niveau du salaire brut, et donc soumis à cotisations sociales et impôt sur le revenu.'

L'employeur justifie le dépassement, alors le montant ayant dépassé la limite d'exonération sera lui aussi exonéré de cotisations sociales et impôt sur le revenu

Avant de passer à d'autres frais professionnels, il faut bien sûr mentionner les frais de nourriture suivants :'

Les repas d'affaires : ils entrent dans la catégorie des frais d'entreprise et sont exonérés de cotisations, de CSG et de CRDS et obéissent à des règles strictes, 
à savoir être exceptionnels, en dehors de l'activité du salarié et dans l'intérêt de l'entreprise, et faire l'objet d'un justificatif.'

Les frais de restaurant : voir ci-dessous "les frais de déplacement".


'Les frais de transport'


Il existe quatre possibilités de frais de transport dans le cadre du transport entre le domicile et le lieu de travail :

Les frais de transport public.

Les frais de transport personnel.

L'indemnité kilométrique vélo.'

Les frais de voiture au titre des frais professionnels.

'Les frais de transport public'
Il s'agit pour le coup d'une participation obligatoire de l'employeur, quelle que soit la position géographique de l'entreprise en France, pour le transport du domicile au lieu de travail.

L'employeur doit donc participer à 50 % aux :'

titres d'abonnement aux transports publics de personnes ;'

titres de services publics de location de vélo.

Cela concerne également les stagiaires.

Les billets à l'unité sont exclus'

La prise en charge doit couvrir l'intégralité du trajet, même si plusieurs abonnements sont nécessaires.'

L'obligation est la même pour les salariés à temps partiel que pour les salariés à temps plein, sans prorata.'


'Les frais de transport personnel'
On peut aussi parler de "prime transport".

Le principe ici, contrairement aux frais de transport public, est que la participation de l'employeur à ces frais est facultative.'

Cette participation aux frais n'est possible que pour les salariés qui sont obligés d'utiliser leur véhicule personnel pour se rendre à leur lieu de travail :

leur résidence habituelle ou leur lieu de travail est situé en dehors de la région Île-de-France, ou d’une zone couverte par les transports urbains ;

les horaires de travail ne leur permettent pas d’utiliser les transports en commun.

Ces frais sont :

exonérés de toute cotisation et de toute contribution légale ou conventionnelle, limité à 200 € par salarié et par an ;

exonérés d'impôt sur le revenu, limité à 200 € par salarié et par an.'

Le montant pris en charge par l'employeur doit absolument figurer dans une rubrique identifiée clairement sur le bulletin de salaire.'

L'indemnité kilométrique vélo'
Tout comme pour les frais de transport personnel, la participation de l'employeur à l'indemnité kilométrique vélo de ses salariés est ici encore facultative.

afin de faire le trajet entre son domicile et son lieu de travail, et inversement.

La participation de l'employeur se fait sous forme de ce qu'on appelle une "indemnité kilométrique vélo", à raison de 25 centimes par kilomètre, 
selon les articles L 3261-3-1 et D 3261-15-1 du Code du travail.

Source : https://www.urssaf.fr.

Il peut y avoir un cumul de cette participation de l'employeur et d'un remboursement au titre des frais de transport public, en cas de trajet jusqu'à la gare ou la station concernée.'

Cette participation est :

exonérée de toute cotisation et de toute contribution légale ou conventionnelle, limité à 200 € par salarié et par an ;

exonérée d'impôt sur le revenu, à hauteur de 200 € par salarié et par an.'

Le montant pris en charge par l'employeur doit absolument figurer dans une rubrique identifiée clairement sur le bulletin de salaire.'


'Les frais de voiture au titre des frais professionnels'

Il s'agit ici de cas où l'employeur décide d'aller au-delà de la prime transport, pour les salariés étant dans l'obligation d'utiliser leur véhicule personnel pour se rendre à leur lieu de travail.'

On peut distinguer deux cas de figure.

1. Le salarié utilise son véhicule pour se rendre à son lieu de travail par "convenance personnelle".

Dans ce cas, la participation de l'employeur aux indemnités de transport n'est exonérée que dans la limite du tarif du transport en commun le plus économique. 
De plus, le salarié n'est pas éligible à la prime transport.'

2. Le salarié utilise son véhicule par contrainte.

Dans ce cas, l'exonération est à hauteur des barèmes kilométriques émis par l'administration fiscale.

Source : https://www.service-public.fr.


S'il y a cumul entre la prime transport et l'indemnité kilométrique, alors l'exonération peut aller au-delà de 200 € par salarié et par an, '
mais dans la limite des frais réellement engagés par le salarié pour ses trajets entre son domicile et son lieu de travail.


Cela implique donc évidemment d'être en mesure de présenter les justificatifs des frais en question.'


Présentation d'autres catégories de frais professionnels'

'Les frais de déplacement (restaurant, transport, hôtel)'

Nous nous trouvons ici dans une situation bien spécifique, au cours de laquelle le salarié doit changer de lieu de résidence en raison du déplacement de son poste de travail.

La mutation et le déménagement peuvent s'accompagner de frais de déménagement '

Il n'y a en effet pas de possibilité de rembourser ces frais sous forme forfaitaire.'


'Le télétravail'
Lorsqu'un salarié est en situation de télétravail, les frais qu'il engage sont considérés comme des charges de caractère spécial inhérentes à la fonction ou à l’emploi.


'Les nouvelles technologies'

L'employeur doit donc rembourser ces frais tout en apportant la justification de la réalité de ces dépenses professionnelles, telles qu'elles ont été engagées par le salarié.


'Les vêtements'

Ces vêtements sont la propriété de l’employeur. Ils ne sont donc pas destinés à être portés en dehors du lieu de travail. Dans le cas contraire, il faudrait les passer en avantage en nature.


En résumé
Certains éléments de rémunération viennent compenser les dépenses du salarié par rapport à l'exercice de son travail.'

D'autres éléments vont servir à le rembourser pour des frais engagés dans le cadre de l'exercice de son travail, à titre usuel ou exceptionnel.

Ces éléments vont par leur nature pouvoir bénéficier d'exonération des cotisations sociales et autres contributions, mais également d'impôt sur le revenu.

En revanche, ces éléments sont soumis à des règles strictes au niveau des limites d'exonération.'


'Gérez les événements impactant le salaire net'

Ces différents mécanismes ont un impact sur la partie nette du salaire, c'est-à-dire après déduction des cotisations sociales, de la CSG et de la CRDS.'

On peut distinguer notamment :

l'avance sur salaire ;'

l'acompte ;'

la saisie des rémunérations.

'L’avance sur salaire'

Il s’agit d’un “versement par l’employeur d’une somme qui correspond à un travail non encore effectué par le salarié”.

Cet élément est à ne pas confondre avec 'l’acompte', qui est un paiement en avance d’un travail déjà effectué.

Exemple :

Un salarié demande à son employeur de lui verser un montant de son salaire d'avril sur la paie de mars. Le mois d'avril n'étant pas encore écoulé, '
il s'agit typiquement d'une demande d'avance, puisque le travail d'avril n'a pas encore été effectué.'


Un salarié peut avoir sur la même période plusieurs retenues :

remboursement d’une avance ;

remboursement d’un acompte ;

retenue au titre d’une saisie sur rémunération, aussi appelée saisie sur salaire ou saisie arrêt.

La retenue effectuée au titre de l'avance sur salaire apparaît sur le bulletin de paie dans une rubrique spécifique située après le salaire net imposable.'

'L’acompte'

Contrairement à l’avance sur salaire, l’acompte “consiste à verser à un salarié la rémunération d’une période de travail déjà effectuée avant son échéance normale”.

Exemple :

On parle d'acompte si le salarié demande à ce que les deux premières semaines du mois de mars lui soient payées le 15 et non pas le 31, '
comme il est d'usage dans son entreprise. Le travail a déjà été effectué lorsqu'il lui sera versé.

L’acompte n’est pas soumis à cotisations sociales au moment du versement. 
Ceci s’explique notamment par le fait qu’il s’agit d’un versement du salaire que le salarié aurait dû percevoir plus tard, autrement dit d’un versement en net.

Sur le bulletin de paie, au même titre que l'avance sur salaire, l'acompte doit apparaître de manière explicite dans une rubrique dédiée à cet effet.

'La saisie des rémunérations'

Cela concerne toute situation dans laquelle le salarié serait débiteur et que son créancier, c'est-à-dire la personne à qui il doit de l'argent, 
décide de se faire rembourser en demandant à l'employeur du salarié concerné d'opérer des retenues sur la rémunération nette qui devrait normalement être payée au salarié.

Il existe trois procédures de retenue sur la rémunération due au salarié :

la saisie des rémunérations ;

la demande de paiement direct de pension alimentaire ;

l'avis à tiers détenteur.'

'La saisie des rémunérations'

L'entreprise du salarié va donc recevoir une notification du greffe du tribunal d'instance, sous forme d'un acte de saisie des rémunérations'

Il faut bien noter les informations qui doivent absolument apparaître sur l'acte en question :'

l’identification et les coordonnées du débiteur et du créancier ;

le décompte des sommes concernées par la saisie ;

le mode de calcul de 'la quotité saisissable' du salaire et les modalités de son versement.

En tant que gestionnaire de paie, il sera indispensable de vérifier 'la quotité saisissable'. C'est donc un des points de contrôle essentiels en matière de saisie des rémunérations.'

'La demande de paiement direct de pension alimentaire'

C'est une procédure qui peut être mise en place par le bénéficiaire d'une pension alimentaire, 
à qui le salarié n'aurait pas versé de pension à échéance. Le créancier peut alors mettre en place une procédure de paiement direct de pension alimentaire.'

L'avis à tiers détenteur'
Cette procédure concerne les dettes fiscales du salarié.

Que se passe-t-il en cas de plusieurs saisies simultanées ?
On met alors en place un système de priorisation :

La procédure de paiement direct de pension alimentaire.

La procédure d'avis à tiers détenteur.'

La procédure de saisie des rémunérations.


Dans ce cas, c'est le tribunal d'instance qui gère le montant des saisies à opérer et la redistribution aux créanciers, une fois les montants versés par l'employeur.'


'Comment répercuter ces éléments sur le bulletin de paie ?'
Sur le bulletin de paie, ce genre d'élément de rémunération doit être traité de la manière suivante :'

rubrique spécifique ;

la nature de la retenue doit être indiquée ;

le montant exact de la retenue doit apparaître.

La rémunération d'un salarié ne peut jamais être saisie en totalité.'

Afin de pouvoir calculer le montant qui peut être saisi chaque mois, aussi appelé "quotité saisissable", un barème a été mis en place. Il a changé au 1er janvier 2020 :

Ce barème concerne en principe les éléments de rémunération et certains revenus de substitution, mais pas toutes les sommes versées à un salarié :

Certaines sommes sont insaisissables, comme "les remboursements de frais."


Il y a également des éléments qui sont totalement insaisissables dans le cadre d'une procédure de saisie des rémunérations, '
mais qui peuvent l'être dans le cadre de procédures telles que celle d'un avis à tiers détenteur : 
'indemnités de licenciement, dommages-intérêts ou indemnités de mise à la retraite,' par exemple.


Depuis le 1er janvier 2019, le montant du prélèvement à la source devra également être déduit du salaire brut, au même titre que les cotisations sociales, la CSG et la CRDS, 
afin de déterminer 'la quotité saisissable.'

Cela signifie que l'impôt sur le revenu est prioritaire par rapport aux saisies sur rémunérations.'

"En résumé"
Il existe des mécanismes impactant directement le salaire net de l'employé.'

L'avance sur salaire et l'acompte permettent de recevoir une fraction de la rémunération nette mensuelle par anticipation.

Les différentes procédures de saisie des rémunérations permettent aux créanciers d'être remboursés par le biais de l'employeur, directement sur le montant net du salaire.



"Identifier et calculer les variables impactant le net"

Question 1
Qu'est-ce qu'un avantage en nature ?

# C'est une rémunération en espèces
# Il s'agit d'un élément de rémunération similaire à une prime
C'est une prestation fournie par l’employeur au salarié pour lui éviter une dépense'

'Un avantage en nature' est une prestation fournie par l’employeur au salarié, lui évitant ainsi une dépense.

Question 2
Vrai ou faux ? Un avantage en nature est soumis à cotisations et charges sociales.

Vrai

En tant qu'élément de rémunération, il doit être traité comme du salaire et est donc soumis à cotisations sociales et autres charges.'

Question 3
Comment est calculé l'avantage en nature au niveau du salaire net ?'
# L'avantage en nature est un élément qui est payé au salarié
# L'avantage en nature est passé en négatif au niveau du salaire brut et en positif au niveau du salaire net
L'avantage en nature n'est pas payé au salarié et est donc déduit avant le salaire net

L'avantage en nature est par définition une rémunération en nature. Cela signifie que le salarié ne doit pas recevoir de salaire en plus de la prestation fournie par son employeur. '
Une fois les cotisations sociales et autres charges calculées, le montant de l'avantage en nature doit donc être déduit avant le salaire net sur le bulletin de salaire.'

Question 4
Que sont les frais professionnels?
# Ce sont des frais retenus par l'employeur sur le bulletin de son salarié, au titre de son travail effectif
# Il s'agit d'indemnités versées par l'employeur à son salarié

Des dépenses faites par le salarié de par la nature de son travail
L'arrêté du 20 décembre 2002 définit à son article 1 les frais professionnels comme des "charges de caractère spécial inhérentes à la fonction ou à l’emploi du salarié, '
que celui-ci supporte au titre de l’accomplissement de ses fonctions"."

Question 5
Vrai ou faux ? En principe, les frais professionnels ne peuvent pas être intégrés à la rémunération du salarié.
Vrai
En principe, le remboursement des frais professionnels ne peut pas être intégré à la rémunération du salarié. 
Il peut toutefois exister une exception, moyennant le respect de certaines conditions.

Question 6
Quels éléments ci-dessous entrent dans la catégorie des frais professionnels ?

Attention, plusieurs réponses sont possibles.
# Les avantages en nature
# Les saisies sur rémunération
Les frais de transport
Les frais de restauration
Les frais de transport et de nourriture du salarié dans le cadre de son activité professionnelle sont typiquement des frais professionnels, 
au titre de l'article 1 de l'arrêté du 20 décembre 2002.

Question 7
Qu'est-ce qu'une avance sur salaire ?

# Un rappel de salaire
# Un paiement en avance d’un travail déjà effectué
Un versement d’une somme qui correspond à un travail non encore effectué par le salarié
Une avance sur salaire est un versement par l’employeur d’une somme qui correspond à un travail non encore effectué par le salarié.

Question 8
Qu'est-ce qu'un acompte ?
# Un versement d’une somme qui correspond à un travail non encore effectué par le salarié
# Une prime de résultat
Une rémunération d’une période de travail déjà effectuée, avant son échéance normale
L'acompte consiste à verser à un salarié la rémunération d’une période de travail déjà effectuée, avant son échéance normale.'

Question 9
Comment définir la saisie sur rémunération ?
# Il s'agit d'une situation de créance du salarié
# Il s'agit d'une dette du salarié envers son employeur
C'est la retenue d'une dette directement sur le salaire net du salarié
Il s'agit d'une retenue sur la rémunération nette qui devrait normalement être payée au salarié, afin de payer tout ou partie de sa dette à son créancier, via son employeur.

Question 10
Vrai ou faux ? L'avis à tiers détenteur est une forme de saisie sur rémunération.'
Vrai
L'avis à tiers détenteur concerne les dettes fiscales du salarié, qui peuvent donc être déduites directement sur son bulletin de salaire en tant que saisie sur rémunération.'


"Maîtrisez les différents plans d'épargne en entreprise'"

Dans un premier temps, il faut préciser ce qu'est un plan d'épargne entreprise.

D'après l'article L 3332-1 du Code du travail, le plan d'épargne entreprise consiste en '
un "système d’épargne collectif permettant aux salariés de constituer un portefeuille de valeurs mobilières avec l’aide de l’entreprise"


Les nouveaux plans d'épargne retraite d'entreprise (PERE) au 1er octobre 2019 :

le PERE-CO (plan d'épargne retraite d'entreprise collectif) ;

le PERE-OB (plan d'épargne retraite d'entreprise obligatoire).

Nous pouvions jusqu'alors distinguer trois catégories de plan d'épargne :

le plan d'épargne entreprise ;' PEE

le plan d'épargne interentreprises ;' PEI

le plan d'épargne pour la retraite collectif.' PERCO


Le plan d'épargne entreprise (PEE)'
Le plan d'épargne entreprise peut être mis en place par le biais :'

d'un accord avec le personnel ;'
d'une décision unilatérale du chef d'entreprise (pour plus de détails sur ces deux points, vous pouvez aller consulter les articles L 3332-3, L 3332-4 et R 3332-7 du Code du travail).


Comment alimente-t-on un PEE ?
Il y a plusieurs méthodes possibles :
le versement volontaire des adhérents ;
l'intéressement et la participation ;'
l'affectation d'actions gratuites ;
le transfert d'épargne salariale.'
l'abondement de l'employeur ;


Il existe tout de même des cas de "déblocage autorisé anticipé", comme par exemple :
mariage ou conclusion d’un Pacs ;
naissance ou adoption d’un troisième enfant ;
divorce, séparation ou dissolution d’un Pacs, avec la garde d’au moins un enfant ;
invalidité du salarié, de ses enfants, de son conjoint ou de son partenaire dans le cadre d’un Pacs ;
décès du salarié, de son conjoint ou de son partenaire dans le cadre d’un Pacs.

Passons maintenant à un des moyens d'alimentation du PEE qui nous intéressent particulièrement en tant que gestionnaires de paie, à savoir l'abondement employeur.
L'abondement de l'entreprise ne constitue pas un salaire.

L'abondement consiste en un versement direct de l'employeur en plus de ceux opérés par les bénéficiaires. 

Les versements des bénéficiaires concernés sont les suivants :
Les versements volontaires (dont l'intéressement).'
La quote-part de réserve de participation.
Les transferts de montants issus d'un PEE ou d'un PEI à l'issue de leur période d'indisponibilité.
L'affectation d'actions gratuites.

Le règlement d'un PEE doit être déposé auprès de la DREETS. Si ce n'est pas fait,  le dépôt auprès de la DREETS est la garantie des exonérations sociales et fiscales.
alors les abondements versés sur les PEE ne peuvent pas bénéficier 'des exonérations sociales et fiscales' que nous allons voir plus loin dans ce chapitre.
Les bénéficiaires de ce plan sont les salariés de l'entreprise, sans distinction, sauf condition d'ancienneté minimale, qui ne peut pas dépasser 3 mois.
Les montants qui vont être versés sur le PEE sont exonérés socialement et fiscalement s'ils sont bloqués pendant 5 ans.'

Il existe des limites, concernant le montant de l'abondement, à ne pas dépasser. Pour en savoir plus, vous pouvez vous reporter aux articles L 3332-11 et R 3332-8 du Code du travail.'
Le plafond prévu à l'article L. 3332-11 est fixé à 8 % du montant annuel du plafond prévu à l'article L. 241-3 du code de la sécurité sociale.

si les conditions sont remplies :

if abondement_PEE > 8 % Plafond and >= 5 ans and déposé_DREETS:
    result = exonéré es cotisations de Sécurité sociale et autres charges ayant la même assiette and IR
    result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social pour la partie exonérée de cotisations sociales.

La CSG est 'intégralement non déductible', lorsqu’elle porte sur des sommes exonérées à la fois d’impôt sur le revenu et de cotisations de Sécurité sociale.
Cela concerne donc la CSG prélevée sur 'la fraction de l’abondement' exonérée d’impôt et de cotisations de Sécurité sociale.

C'est à ce stade du processus d'épargne que le gestionnaire de paie va devoir intervenir.

Le plan d'épargne interentreprises (PEI)'
Le PEI suit à la fois la réglementation du PEE ou du PERCO, 
Pour en savoir plus, vous pouvez vous référer aux articles L 3333-1 à L 3333-8 d'une part, et R 3333-1 à R 3333-5 d'autre part, du Code du travail.


Le plan d'épargne pour la retraite collectif (PERCO)'
Avant toute chose, il faut préciser qu'un PERCO ne peut être mis en place dans une entreprise que si un plan d'épargne moins long est disponible pour les salariés.
Les formalités de dépôt sont identiques à celles du PEE. 
En principe, les sommes affectées à un PERCO sont bloquées jusqu’au départ à la retraite (article L 3334-14 du Code du travail).

Le PERCO peut être alimenté de différentes façons.

Par les bénéficiaires :
versements volontaires ;
transfert d'épargne ;'
alimentation par le compte épargne-temps (CET) ;
affectation de jours de repos non pris, si l’entreprise n’est pas dotée d’un compte épargne-temps.

Par l'employeur :'
abondement ;
abondement initial (dit versement d’amorce) ou, depuis la loi Macron, versements périodiques de l’employeur.

if abondement_PERCO > 8 % Plafond and >= Age_départ  and déposé_DREETS:
    result = exonéré es cotisations de Sécurité sociale et autres charges ayant la même assiette and IR
    result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social pour la partie exonérée de cotisations sociales.

'Quel est le régime social et fiscal des montants versés sur le PERCO ?'
Ici, en plus de l'abondement de l'employeur, nous mentionnerons :
l'alimentation du PERCO par le compte épargne-temps (CET), '
ainsi que l'affectation de jours de repos pour les entreprises ne disposant pas d'un compte épargne-temps.

L'alimentation par le compte épargne-temps'
Cela concerne les CET permettant d'utiliser une partie ou bien l'intégralité de leurs droits pour effectuer des versements sur un 'PERCO'.

Il y a deux cas de figure :

---------Les droits concernés correspondent à un abondement en temps ou en argent de l'employeur : '
dans ce cas, il faut cumuler les sommes aux abondements directs de l'employeur, et leur appliquer le régime social et fiscal correspondant.'

if CET_PERCO = abondement :
    result = CET_PERCO.append(abondement_PERCO)

---------Les droits affectés au CET ne sont pas issus d'un abondement de l'employeur : 
ils sont alors, dans la limite de 10 jours par an, exonérés d'impôt sur le revenu et de cotisations sociales (salariales et patronales) '
d'assurance maladie, assurance vieillesse et allocations familiales. ' + le forfait social

Les autres charges restent dues (FNAL, versement de transport, contribution solidarité autonomie, CSG/CRDS, cotisation accidents du travail, assurance chômage, 
retraite complémentaire, contribution au dialogue social, cotisations pénibilité...), sauf le forfait social.

if CET_PERCO != abondement:
    result = 10 J/an exonéré es cotisations de Sécurité sociale and IR and Forfait Social
    result = soumis aux autres charges ayant la même assiette 
    # result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social pour la partie exonérée de cotisations sociales. à vérifier ????

L'affectation de jours de repos'
Cela concerne les entreprises n'ayant pas de compte épargne-temps.'

L'article L 3334-8 du Code du travail précise que dans ce genre de situation, les salariés peuvent verser sur un PERCO un montant correspondant à 10 jours par an maximum de repos non pris.'

Dans ce cas, les 10 jours bénéficient d'un régime social et fiscal de faveur, identique à celui exposé ci-dessus, '
à partir du moment où le montant versé ne correspond pas à un abondement de l'employeur.'

En d'autres termes, les sommes :'
sont exonérées d'impôt sur le revenu + le forfait social;'

sont exonérées de cotisations sociales (salariales et patronales) d'assurance maladie, assurance vieillesse et d'allocations familiales. 
En revanche, Les autres charges restent dues (FNAL, versement de transport, contribution solidarité autonomie, CSG/CRDS, cotisation accidents du travail, assurance chômage, 
retraite complémentaire, contribution au dialogue social, cotisations pénibilité...), sauf le forfait social.
ne sont également pas assujetties au forfait social.

if company_id != CET and versement_PERCO != abondement:
    result = 10 J/an exonéré es cotisations de Sécurité sociale and IR and Forfait Social
    result = soumis aux autres charges ayant la même assiette 
    # result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social pour la partie exonérée de cotisations sociales. à vérifier ????

Le régime de l'abondement de l'employeur
L'article L 3332-7 du Code du travail précise que si les conditions requises sont remplies, l’abondement ne constitue pas un salaire, à partir du moment où il ne dépasse pas :'

le triple de la contribution du salarié ;
et 16 % du montant annuel du plafond de la Sécurité sociale (soit 6  581,76 € en 2020).

Ainsi, l’abondement de l’employeur est exonéré :

des cotisations de Sécurité sociale et des charges ayant la même assiette (Fnal, versement de transport, contribution solidarité autonomie, assurance chômage et AGS, 
contribution au dialogue social, cotisations pénibilité, retraite complémentaire, participation à la formation professionnelle, participation à l’effort de construction, taxe d’apprentissage) ;

d’impôt sur le revenu.

En revanche, les cotisations suivantes s'appliquent à l'abondement au plan d'épargne :'
taxe sur les salaires pour les employeurs qui y sont assujettis, depuis le 1er janvier 2013 ;
CSG et CRDS sur les revenus d’activité, sans abattement d’assiette ;
forfait social – la fraction d’abondement exonérée de cotisations de Sécurité sociale mais assujettie à CSG est soumise au forfait social, en principe au taux de 20 %.
La partie de l’abondement qui dépasse le plus bas des deux seuils mentionnés plus haut est soumise à cotisations et imposable.

Sous conditions, un taux réduit de forfait social peut s’appliquer.
Il faut pour cela que le règlement du plan d'épargne respecte deux conditions, précisées à l'article L 137-16 al. 7 du Code de la Sécurité sociale :

"[...]"

1° Les sommes recueillies sont affectées par défaut, dans les conditions prévues au second alinéa de l'article L. 3334-11 du même code.'
2° L'allocation de l'épargne est affectée à l'acquisition de parts de fonds, dans des conditions fixées par décret, '
qui comportent au moins 7 % de titres susceptibles d'être employés dans un plan d'épargne en actions destiné au financement des petites et moyennes entreprises et des entreprises 
de taille intermédiaire, dans les conditions prévues à l'article L. 221-32-2 du Code monétaire et financier."'
Si ces deux conditions sont respectées, alors le taux du forfait social à appliquer sera de 16 %.

Une ordonnance du 24 juillet 2019 précise que les PERCO et contrats de retraite supplémentaire "art. 83" ne pourront plus être mis en place dans les entreprises, 
à partir du 1er octobre 2020. En revanche, ceux qui auront été mis en place avant cette date pourront continuer à accueillir de nouveaux salariés et même de nouveaux versements.  

if abondement_PERCO <= min(3 * COS_PERCO, 16% PASS):
    result = exonéré des cotisations de Sécurité sociale et autres charges ayant la même assiette and IR
    result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social(20%) pour la partie exonérée de cotisations sociales.
else:
a = abondement_PERCO
b = min(3 * COS_PERCO, 16% PASS)
    result = (a-b) => soumis à des cotisations de Sécurité sociale et autres charges ayant la même assiette and IR
    result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social(20%) pour la partie exonérée de cotisations sociales.

if abondement_PE == respecte deux conditions, précisées à l'article L 137-16 al. 7 du Code de la Sécurité sociale':
    result = Forfait Social(16%) 


'Le compte épargne-temps (CET)'
Il peut être utilisé pour :
accumuler des droits à congés rémunérés à utiliser dans l’avenir ;
obtenir un complément de rémunération immédiate (ex. : monétarisation de jours de RTT) ;
alimenter des plans d’épargne ;
financer un système de retraite supplémentaire.
Le CET est soumis à un accord collectif destiné à gérer les règles de gestion du compte.

Traitement sur le bulletin de paie
'Le régime social'
Les sommes issues d'un CET obéissent au principe suivant.'

Les sommes doivent être traitées comme un élément de salaire :
soit au moment du versement des indemnités compensatrices ;
soit au moment du versement du complément de rémunération.

Autrement dit, ces sommes sont assujetties :

à l’ensemble des cotisations (CSG et CRDS incluses) ;
aux taxes et participations assises sur les salaires (participations formation et construction, taxe d’apprentissage, taxe sur les salaires).
Dans le cas de sommes provenant de l’intéressement, de la participation ou de l’abondement de l’employeur à un PEE, 

celles-ci sont soumises à CSG et CRDS sur les revenus d’activité, ainsi qu’au forfait social, au moment de la répartition ou du versement de l'abondement sur le PEE, le cas échéant.'
Par conséquent, elles ne sont pas soumises de nouveau aux mêmes contributions lorsque le salarié utilise son CET comme complément de rémunération 
ou, à l’occasion d’un congé, sous forme d’indemnité compensatrice.

'Le régime fiscal'
Ici, le principe est que les sommes versées aux salariés lors de la mobilisation des droits issus du CET sont soumises à l'impôt sur le revenu.'

Par dérogation, les indemnités compensatrices ou financières correspondant à l’affectation au CET, après leur période d’indisponibilité, de sommes issues de l’épargne salariale, 
sont exonérées d’impôt sur le revenu au moment de leur versement au salarié (cf. l'article L 3343 -1 du Code du travail).'

En revanche, une prime d’intéressement affectée au CET est soumise à l’impôt sur le revenu l’année de son versement au salarié.

if CET :
    result = soumis à des cotisations de Sécurité sociale and ux autres charges ayant la même assiette and IR
    result = soumis à Taxe sur salaire and CSG/CRDS sans abattement and Forfait Social pour la partie exonérée de cotisations sociales. 


'En résumé'
Il existe différentes façons pour le salarié d'épargner au sein de son entreprise.'

Ces plans doivent respecter certaines procédures de mise en place, afin de bénéficier d'exonérations sociales et fiscales.'

Les montants versés sur ces plans doivent être bloqués pendant une certaine durée, et ne doivent pas dépasser un certain pourcentage annuel.













































































































