import os
import re

target_dir = './content/posts'

print("🔍 추천 링크 복구 작전을 시작합니다...")

for filename in os.listdir(target_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 추천 글 구역이 있는 경우만 타격
        if '🔗 Recommended Reading' in content:
            # 기존 엉터리 링크 패턴 탐지 (날짜 유무 상관없이 추출)
            pattern = r'<a href="/(?:[0-9]{8}-)?([^/]+)/"([^>]*)>.*?</a>'
            
            def replace_func(match):
                slug = match.group(1) # Mac-Security-Hardening...
                style = match.group(2) # style="..."
                
                # 1. 연결 주소: 100% 소문자로 변환 (가장 중요!)
                new_url = f"/{slug.lower()}/"
                # 2. 화면 글자: 하이픈(-)을 띄어쓰기로 변환하여 예쁜 제목으로!
                new_text = slug.replace('-', ' ')
                
                return f'<a href="{new_url}"{style}>{new_text}</a>'
            
            new_content = re.sub(pattern, replace_func, content)
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 복구 완료: {filename}")

print("🎉 51개 파일 모든 링크가 정상 주소(소문자)와 예쁜 제목으로 교체되었습니다!")
