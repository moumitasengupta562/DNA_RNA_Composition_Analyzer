# DNA/RNA Composition Analyzer
import pandas as pd
import matplotlib.pyplot as plt

# Function to read sequence from file
def read_sequence(file_path):
    with open(file_path, "r") as f:
        sequence = f.read().replace("\n", "").upper()
    return sequence

# Function to calculate nucleotide composition
def nucleotide_composition(sequence):
    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T") if "T" in sequence else 0,
        "U": sequence.count("U") if "U" in sequence else 0,
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }
    total = sum(counts.values())
    percentages = {k: round(v/total*100, 2) for k, v in counts.items() if v>0}
    return counts, percentages

# Function to plot composition
def plot_composition(percentages, seq_type="DNA/RNA"):
    df = pd.DataFrame(list(percentages.items()), columns=["Nucleotide", "Percentage"])
    plt.figure(figsize=(6,4))
    plt.bar(df["Nucleotide"], df["Percentage"], color=["#FF9999","#66B2FF","#99FF99","#FFCC99","#C2C2F0"])
    plt.title(f"Nucleotide Composition of {seq_type} Sequence")
    plt.ylabel("Percentage (%)")
    plt.show()

# Main
if __name__ == "__main__":
    file_path = "example_sequence.txt"  # input file
    sequence = read_sequence(file_path)
    counts, percentages = nucleotide_composition(sequence)
    
    print("Nucleotide Counts:", counts)
    print("Nucleotide Percentages:", percentages)
    
    seq_type = "RNA" if "U" in sequence else "DNA"
    plot_composition(percentages, seq_type)

