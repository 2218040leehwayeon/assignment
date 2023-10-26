def calculate_risk_priority(s, o, d):
    return s * o * d

def generate_fmea_report(risk_factors):
    print("FMEA 보고서")
    print("---------------------------------------------------")
    print("위험 항목\t심각성 (S)\t발생 빈도 (O)\t탐지 능력 (D)\t위험 우선 순위")
    print("---------------------------------------------------")

    for factor in risk_factors:
        s = float(input(f"위험 항목 '{factor}'의 심각성 (S) 입력: "))
        o = float(input(f"위험 항목 '{factor}'의 발생 빈도 (O) 입력: "))
        d = float(input(f"위험 항목 '{factor}'의 탐지 능력 (D) 입력: "))

        risk_priority = calculate_risk_priority(s, o, d)
        print(f"{factor}\t\t{s}\t\t{o}\t\t{d}\t\t{risk_priority:.2f}")

    print("---------------------------------------------------")

if __name__ == "__main__":
    risk_factors = []

    while True:
        factor = input("위험 항목을 입력하십시오 (종료하려면 'q' 입력): ")
        if factor.lower() == 'q':
            break
        risk_factors.append(factor)

    generate_fmea_report(risk_factors)
