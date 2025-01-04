import React from 'react';
import { Progress } from '@/components/ui/progress';

interface GameProgressProps {
  currentLevel: number;
  totalLevels: number;
}

const GameProgress: React.FC<GameProgressProps> = ({ currentLevel, totalLevels }) => {
  const progress = (currentLevel / totalLevels) * 100;

  return (
    <div className="w-full max-w-md mx-auto mb-8">
      <div className="flex justify-between mb-2">
        <span className="text-retro-primary font-retro text-sm">Level {currentLevel}</span>
        <span className="text-retro-light font-retro text-sm">{Math.round(progress)}%</span>
      </div>
      <Progress value={progress} className="h-4 bg-retro-secondary">
        <div
          className="h-full bg-retro-primary transition-all duration-500"
          style={{ width: `${progress}%` }}
        />
      </Progress>
    </div>
  );
};

export default GameProgress;