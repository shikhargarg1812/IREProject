

import json
from rouge import Rouge
import argparse
import matplotlib.pyplot as plt


Rouge.DEFAULT_METRICS = ["rouge-1", "rouge-2", "rouge-3", "rouge-l"]


def get_rouge_scores(summary_json_file, output_json_file):
    rouge = Rouge()
    data = json.load(open(summary_json_file, 'r'))
    new_data = []
    ctr = 0
    for paper in data:
        abstract, summary = paper["abstract"], paper["transcript"]
        print(abstract, summary)
        if summary != "NA":
                scores = rouge.get_scores(abstract, summary)
                new_data.append({
                    "ctr": ctr,
                    "title": paper["paper_title"],
                    "rouge_scores": scores
                })
                ctr += 1
    fp = open(output_json_file, 'w')
    json.dump(new_data,fp)
    fp.close()

def plot_distributions(output_json_file):
    data = json.load(open(output_json_file,'r'))
    p2 = [item['rouge_scores'][0]['rouge-1']['p'] for item in data]
    r2 = [item['rouge_scores'][0]['rouge-1']['r'] for item in data]
    f2 = [item['rouge_scores'][0]['rouge-1']['f'] for item in data]
    p3 = [item['rouge_scores'][0]['rouge-2']['p'] for item in data]
    r3 = [item['rouge_scores'][0]['rouge-2']['r'] for item in data]
    f3 = [item['rouge_scores'][0]['rouge-2']['f'] for item in data]
    pl = [item['rouge_scores'][0]['rouge-l']['p'] for item in data]
    rl = [item['rouge_scores'][0]['rouge-l']['r'] for item in data]
    fl = [item['rouge_scores'][0]['rouge-l']['f'] for item in data]
    plt.figure(figsize=(12,8))
    plt.subplot(1,3,1)
    plt.hist(p2)
    plt.title("Rouge-2P distribution")
    plt.subplot(1,3,2)
    plt.hist(r2)
    plt.title("Rouge-2R distribution")
    plt.subplot(1,3,3)
    plt.hist(f2)
    plt.title("Rouge-2F distribution")
    plt.savefig("rouge2.png")


    plt.figure(figsize=(12,8))
    plt.subplot(1,3,1)
    plt.hist(pl)
    plt.title("Rouge-P-LCS distribution")
    plt.subplot(1,3,2)
    plt.hist(rl)
    plt.title("Rouge-R-LCS distribution")
    plt.subplot(1,3,3)
    plt.hist(fl)
    plt.title("Rouge-F-LCS distribution")
    plt.savefig("rougeLCS.png")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary_json_file", type=str, default="../conference_website/nips_2019_v2.json")
    parser.add_argument("--output_json_file", type=str, default="../conference_website/nips_rouge_scores.json")
    args = parser.parse_args()
    # get_rouge_scores(args.summary_json_file, args.output_json_file)
    plot_distributions(args.output_json_file)

if __name__=="__main__":
    main()