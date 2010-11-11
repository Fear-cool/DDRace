/* copyright (c) 2007 rajh and gregwar. Score stuff */
#ifndef GAME_SERVER_GAMEMODES_RACE_H
#define GAME_SERVER_GAMEMODES_RACE_H

#include <game/server/gamecontroller.h>

class CGameControllerFRACE : public IGameController
{
public:
	
	CGameControllerFRACE(class CGameContext *pGameServer);
	~CGameControllerFRACE();
	
	vec2 *m_pTeleporter;
	
	void InitTeleporter();
	
	virtual void Tick();
	virtual int OnCharacterDeath(class CCharacter *pVictim, class CPlayer *pKiller, int Weapon);
};

#endif
