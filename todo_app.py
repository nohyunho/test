class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """할 일 추가"""
        self.tasks.append({"task": task, "completed": False})
        print(f"✓ '{task}' 추가되었습니다.")
    
    def complete_task(self, index):
        """할 일 완료 처리"""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"✓ '{self.tasks[index]['task']}' 완료!")
        else:
            print("❌ 유효하지 않은 번호입니다.")
    
    def show_tasks(self):
        """모든 할 일 보기"""
        if not self.tasks:
            print("📝 할 일이 없습니다.")
            return
        
        print("\n=== 할 일 목록 ===")
        for i, task in enumerate(self.tasks):
            status = "✅" if task["completed"] else "⬜"
            print(f"{i + 1}. {status} {task['task']}")
        print()
    
    def remove_task(self, index):
        """할 일 삭제"""
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️ '{removed['task']}' 삭제되었습니다.")
        else:
            print("❌ 유효하지 않은 번호입니다.")


def main():
    todo = TodoList()
    
    while True:
        print("\n--- 할 일 관리 ---")
        print("1. 할 일 추가")
        print("2. 할 일 완료")
        print("3. 할 일 목록 보기")
        print("4. 할 일 삭제")
        print("5. 종료")
        
        choice = input("\n선택하세요 (1-5): ")
        
        if choice == "1":
            task = input("추가할 할 일: ")
            todo.add_task(task)
        
        elif choice == "2":
            todo.show_tasks()
            try:
                index = int(input("완료할 번호: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("❌ 숫자를 입력하세요.")
        
        elif choice == "3":
            todo.show_tasks()
        
        elif choice == "4":
            todo.show_tasks()
            try:
                index = int(input("삭제할 번호: ")) - 1
                todo.remove_task(index)
            except ValueError:
                print("❌ 숫자를 입력하세요.")
        
        elif choice == "5":
            print("👋 프로그램을 종료합니다.")
            break
        
        else:
            print("❌ 1-5 사이의 숫자를 입력하세요.")


if __name__ == "__main__":
    main()
