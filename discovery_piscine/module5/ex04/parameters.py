#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] her zaman dosyanın kendi adıdır, bu yüzden onu listeden çıkarıyoruz.
#bu fonksiyon sayesinde kaç tane parametre girdiğimiz anlaşılır
    num_params = len(sys.argv) - 1
    print(f"Number of parameters: {num_params}.")

if __name__ == "__main__":
    main()
