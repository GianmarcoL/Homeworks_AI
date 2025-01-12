"""Score Analysis Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
def analyze_scores(scores):
    num_students, num_subjects = scores.shape #prendo le dimensioni

    #calcoli
    student_averages = np.mean(scores, axis=1) #calc media per asse verticale
    subject_averages = np.mean(scores, axis=0) #calc media per asse orizzontale
    student_stds = np.std(scores, axis=1)  # per la dev standard

    #plotto
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Students scores")

    #subplot stats studenti
    axes[0, 0].bar(range(num_students), student_averages, yerr=student_stds, capsize=5)
    axes[0, 0].set_xlabel("Student")
    axes[0, 0].set_ylabel("Avg")
    axes[0, 0].set_title("Students average")
    axes[0, 0].set_xticks(range(num_students)) #creo la seq da 0 a num_students-1

    #subplot stats materie
    axes[0, 1].bar(range(num_subjects), subject_averages)
    axes[0, 1].set_xlabel("Subject")
    axes[0, 1].set_ylabel("Avg")
    axes[0, 1].set_title("Subjects averages")
    axes[0, 1].set_xticks(range(num_subjects))

    #subplot istogramma punteggi
    axes[1, 0].hist(scores.flatten(), bins=10, edgecolor='black')
    axes[1, 0].set_xlabel("Scores")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].set_title("Scores distribution")

    #box plot per ogni materia
    axes[1, 1].boxplot([scores[:, i] for i in range(num_subjects)], labels=range(num_subjects))
    axes[1, 1].set_xlabel("Subject")
    axes[1, 1].set_ylabel("Score")
    axes[1, 1].set_title("Box plots for every subject")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) #semplicemente un aggiustamento per evitare un overlap delle scritte del subplot
    plt.show()
    pass
