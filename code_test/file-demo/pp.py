from pathlib import Path
path = Path('score.txt')
student_list = []

for line in path:
    line = line.strip()

    if not line:
            continue
        
    fields = line.split(",")

    name = fields[0].strip()
    cls = fields[1].strip()

    score_fields = fields[2:]
        
    valid_scores = []

    for s in score_fields:

        if not s:
                continue

        try:
                score = float(s)
        except ValueError:
                
                continue
            
        if 0 <= score <= 100:
                valid_scores.append(score)
        
    
        if len(valid_scores) >= 1:
            stu_dict = {
                "name": name,
                "class": cls,
                "scores": valid_scores
            }
            student_list.append(stu_dict)

def analyze(students):

    class_stu_avg = {}   
    all_total = []        
    all_valid_scores = [] 

    for stu in students:
        name = stu['name']
        cls = stu['class']
        scores = stu['scores']
        stu_avg = sum(scores) / len(scores)
        stu_total = sum(scores)


        if cls not in class_stu_avg:
            class_stu_avg[cls] = []
        class_stu_avg[cls].append(stu_avg)


        all_total.append((name, cls, stu_total))

        all_valid_scores.extend(scores)

    class_avg = {}
    for c, avg_list in class_stu_avg.items():
        c_avg = sum(avg_list) / len(avg_list)
        class_avg[c] = round(c_avg, 2)

    class_ranking = sorted(class_avg.items(), key=lambda x: x[1], reverse=True)

    top_students = sorted(all_total, key=lambda x: x[2], reverse=True)[:10]

    bottom_students = sorted(all_total, key=lambda x: (x[2], x[0]))[:10]

    max_score = max(all_valid_scores)
    min_score = min(all_valid_scores)
    avg_score = sum(all_valid_scores) / len(all_valid_scores)
    subject_stat = {
        'max': round(max_score, 2),
        'min': round(min_score, 2),
        'avg': round(avg_score, 2)
    }

    return {
        'class_avg': class_avg,
        'class_ranking': class_ranking,
        'top_students': top_students,
        'bottom_students': bottom_students,
        'subject_stat': subject_stat
    }

