english = int(input())
roll_english = set(map(int, input().split()))
french = int(input())
roll_french = set(map(int, input().split()))
print(len(roll_english.symmetric_difference(roll_french)))

