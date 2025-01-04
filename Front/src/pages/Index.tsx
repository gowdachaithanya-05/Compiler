import React from 'react';
import GameLevel from '@/components/GameLevel';
import GameProgress from '@/components/GameProgress';

const LEVELS = [
  {
    code: `#include <stdio.h>
int main() {
  printf("Hello World")
  return 0;
}`,
    solution: `#include <stdio.h>
int main() {
  printf("Hello World");
  return 0;
}`,
    hint: "Check the punctuation! C statements need a specific character at the end.",
  },
  {
    code: `#include <stdio.h>
int main() {
  int x = 5
  int y = 10;
  printf("%d", x + y);
  return 0;
}`,
    solution: `#include <stdio.h>
int main() {
  int x = 5;
  int y = 10;
  printf("%d", x + y);
  return 0;
}`,
    hint: "Look carefully at the first variable declaration. Is it properly terminated?",
  },
  {
    code: `#include <stdio.h>
int main() {
  for(int i = 0; i < 5; i++) {
    printf("%d", i)
  }
  return 0;
}`,
    solution: `#include <stdio.h>
int main() {
  for(int i = 0; i < 5; i++) {
    printf("%d", i);
  }
  return 0;
}`,
    hint: "Check the printf statement inside the loop. Is it properly terminated?",
  },
];

const Index = () => {
  const [currentLevel, setCurrentLevel] = React.useState(1);

  const handleLevelComplete = () => {
    if (currentLevel < LEVELS.length) {
      setCurrentLevel(prev => prev + 1);
    }
  };

  return (
    <div className="min-h-screen bg-retro-dark px-4 py-6 sm:p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-xl sm:text-3xl font-retro text-retro-primary text-center mb-6 sm:mb-8">
          C-Syntax Adventure
        </h1>
        
        <GameProgress currentLevel={currentLevel} totalLevels={LEVELS.length} />
        
        <GameLevel
          level={currentLevel}
          code={LEVELS[currentLevel - 1].code}
          solution={LEVELS[currentLevel - 1].solution}
          hint={LEVELS[currentLevel - 1].hint}
          onComplete={handleLevelComplete}
        />
        
        <div className="mt-6 sm:mt-8 text-center">
          <p className="text-xs sm:text-sm text-retro-light font-retro">
            Fix the syntax errors to advance to the next level!
          </p>
        </div>
      </div>
    </div>
  );
};

export default Index;