def merge(L, R, asc=True):
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if (asc and L[i] <= R[j]) or (not asc and L[i] >= R[j]):
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
    return res + L[i:] + R[j:]

def merge_sort(A, asc=True):
    if len(A) <= 1: return A
    m = len(A) // 2
    return merge(merge_sort(A[:m], asc), merge_sort(A[m:], asc), asc)

def read_numbers(filename):
    try:
        with open(filename) as f:
            return [int(l.strip()) for l in f if l.strip()]
    except:
        print(f"Error reading '{filename}'"); exit()

def main():
    fname = input("Filename: ")
    if not fname: return
    
    nums = read_numbers(fname)
    print(f"Read {len(nums)} numbers")
    
    asc = input("Ascending (y/n)? ").lower() != 'n'
    sorted_nums = merge_sort(nums, asc)
    
    print("First 10 sorted:", sorted_nums[:10])
    
    if input("Save? (y/n): ").lower() == 'y':
        with open(f"sorted_{fname}", 'w') as f:
            for n in sorted_nums: f.write(f"{n}\n")
        print("Saved!")

main()